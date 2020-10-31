#
# ~/.bash_profile
#
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
export PATH="$PATH:$(yarn global bin)"
export PATH=~/.gem/ruby/2.7.0/bin:$PATH
export GEM_PATH=$GEM_PATH:~/.gem/ruby/2.7.0:/usr/lib/ruby/gems/2.7.0

export BROWSER=vivaldi-stable

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias nvsettings='optirun -b none nvidia-settings -c :8'
alias wgstr="sudo systemctl start wg-quick@vpn"
alias wgstp="sudo systemctl stop wg-quick@vpn"
alias jstr="systemctl  start jellyfin.service"
alias jstp="systemctl stop jellyfin.service"
alias jss="systemctl status jellyfin.service"
alias gsynctags="git tag -l | xargs git tag -d && git fetch -t"

complete -d cd
 