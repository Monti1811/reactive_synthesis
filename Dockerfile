FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    g++ \
    wget \
    git

# Create tool location
WORKDIR /

# Install Haskell stack
RUN wget -qO- https://get.haskellstack.org/ | sh

# Install Syfco
RUN git clone https://github.com/reactive-systems/syfco.git syfco-dir
RUN cd syfco-dir && make && cd .. && mv syfco-dir/syfco ./

# Download strix
RUN wget https://github.com/meyerphi/strix/releases/download/21.0.0/strix-21.0.0-1-x86_64-linux.tar.gz
RUN gunzip strix-21.0.0-1-x86_64-linux.tar.gz
RUN tar xfv strix-21.0.0-1-x86_64-linux.tar
RUN chmod +x strix 
RUN rm strix-21.0.0-1-x86_64-linux.tar

# Create running script
RUN echo \
"#!/usr/bin/bash \n\
TLSF=\$(mktemp --suffix .tlsf) \n\
tee \$TLSF > /dev/null \n\
INS=\$(/syfco -f ltl --print-input-signals \$TLSF) \n\
OUTS=\$(/syfco -f ltl --print-output-signals \$TLSF) \n\
LTL=\$(/syfco -f ltl -q double -m fully \$TLSF) \n\
/strix --ins \"\$INS\" --outs \"\$OUTS\" -f \"\$LTL\" \"\$@\" \n\
" >  /synthesize

RUN chmod +x synthesize
