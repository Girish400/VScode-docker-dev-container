FROM python:3.10.0-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .

RUN python -m pip install -r requirements.txt

RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID


RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo wget \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME 



RUN apt-get install -y  \
    git \
    zsh \
    vim 

USER $USERNAME

RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k \
    && echo "source ~/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc \
    && cd ~/powerlevel10k \    
    && echo 'alias cls="clear"' >> ~/.zshrc \
    && exec zsh \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* 

ENTRYPOINT [ "/bin/zsh" ]
CMD ["-l"]