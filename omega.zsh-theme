# git plugin configuration

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[red]%}[%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$fg[red]%}]%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[red]%}!"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg[red]%}?"
ZSH_THEME_GIT_PROMPT_CLEAN=""

# prompt variables

setopt prompt_subst
local omega='%{$fg[red]%}%{$reset_color%}'
local user='%{$fg_bold[white]%}%n@%{$fg[white]%}%m%{$reset_color%}'
local line=$'\n'

# actual prompt
precmd () {
if $(git rev-parse --is-inside-work-tree >/dev/null 2>&1)
then
    PROMPT=" ${omega} ${user} ~ ${line} \$(git_prompt_info) "
else
    PROMPT=" ${omega} ${user} ~ "
fi

}
