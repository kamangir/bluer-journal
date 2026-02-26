#! /usr/bin/env bash

function bluer_journal_git_pull() {
    local options=$1
    local do_pull=$(bluer_ai_option_int "$options" pull 1)
    local is_token=$(bluer_ai_option_int "$options" token 0)

    if [[ -z "$BLUER_JOURNAL_REPO" ]]; then
        bluer_ai_log_error "BLUER_JOURNAL_REPO is not set."
        return 1
    fi

    if [[ ! -d "$abcli_path_git/$BLUER_JOURNAL_REPO" ]]; then
        if [[ "$abcli_is_github_workflow" == true ]]; then
            pushd $abcli_path_git >/dev/null
            if [[ "$is_token" == 1 ]]; then
                bluer_ai_eval - \
                    git clone https://x-access-token:$BLUER_AI_GITHUB_TOKEN@github.com/kamangir/$BLUER_JOURNAL_REPO.git
            else
                bluer_ai_eval - \
                    git clone https://github.com/kamangir/$BLUER_JOURNAL_REPO.git
            fi
            [[ $? -ne 0 ]] && return 1
            popd >/dev/null
        else
            bluer_ai_git_clone $BLUER_JOURNAL_REPO
            [[ $? -ne 0 ]] && return 1
        fi
    fi

    [[ "$do_pull" == 0 ]] &&
        return 0

    bluer_ai_git \
        $BLUER_JOURNAL_REPO \
        pull \
        ~all
}
