# Omega Theme

PROMPT=$'%F{red}┌[%F{white}%n%f%F{red}@%F{white}%m%f%F{red}]
%F{red}└[%f %F{white}%2~%f%F{red}]%f '

path+=('/home/syndrome/bin')

### set common functions

function extract {
 if [ -z "$1" ]; then
    # display usage if no parameters given
    echo "Usage: extract <path/file_name>.<zip|rar|bz2|gz|tar|tbz2|tgz|Z|7z|xz|ex|tar.bz2|tar.gz|tar.xz>"
 else
    if [ -f $1 ] ; then
        # NAME=${1%.*}
        # mkdir $NAME && cd $NAME
        case $1 in
          *.tar.bz2)   tar xvjf $1    ;;
          *.tar.gz)    tar xvzf $1    ;;
          *.tar.xz)    tar xvJf $1    ;;
          *.lzma)      unlzma $1      ;;
          *.bz2)       bunzip2 $1     ;;
          *.rar)       unrar x -ad $1 ;;
          *.gz)        gunzip $1      ;;
          *.tar)       tar xvf $1     ;;
          *.tbz2)      tar xvjf $1    ;;
          *.tgz)       tar xvzf $1    ;;
          *.zip)       unzip $1       ;;
          *.Z)         uncompress $1  ;;
          *.7z)        7z x $1        ;;
          *.xz)        unxz $1        ;;
          *.exe)       cabextract $1  ;;
          *)           echo "extract: '$1' - unknown archive method" ;;
        esac
    else
        echo "$1 - file does not exist"
    fi
fi
}


# Creates an archive (*.tar.gz) from given directory.
function maketar() { tar cvzf "${1%%/}.tar.gz"  "${1%%/}/"; }

# Create a ZIP archive of a file or folder.
function makezip() { zip -r "${1%%/}.zip" "$1" ; }


function my_ps() { ps $@ -u $USER -o pid,%cpu,%mem,bsdtime,command ; }

mkcd () {
    mkdir -p $1
    cd $1
}

### Set alias
#############
alias ..="cd .."
alias cd..="cd .."
alias ll="ls -lisa --color=auto"
alias ls="ls -CF --color=auto"
alias home="cd ~"
alias mkdir="mkdir -pv"
alias rm="rm -rfv"
alias wget="wget -c"
alias myip="curl http://ipecho.net/plain; echo"
alias grep='grep --color=auto'

alsi -l
