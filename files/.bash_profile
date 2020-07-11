#
# ~/.bash_profile
#

export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
export PATH="$PATH:$(yarn global bin)"
export PATH=~/.npm-global/bin:$PATH

alias ratioghost="wish /home/ahmed/Public/ratioghost/rghost.vfs/main.tcl"
export BROWSER=vivaldi-stable

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias nvsettings='optirun -b none nvidia-settings -c :8'
alias wgstr="sudo systemctl start wg-quick@laptop"
alias wgstp="sudo systemctl stop wg-quick@laptop"
complete -d cd

