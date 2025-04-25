#! /usr/bin/env bash

function bluer_journal_check() {
    local repo_name
    for repo_name in \
        $BLUER_JOURNAL_REPO \
        $BLUER_JOURNAL_REPO.wiki; do
        if [[ ! -d "$abcli_path_git/$repo_name" ]]; then
            bluer_ai_git_clone $repo_name
            [[ $? -ne 0 ]] && return 1
        fi
    done

    return 0
}
