#! /usr/bin/env bash

function bluer_journal_validate() {
    if [[ ! -d "$abcli_path_git/$BLUER_JOURNAL_REPO" ]]; then
        abcli_log_error "@journal: repo not found, try running '@git clone $BLUER_JOURNAL_REPO' first."
        return 1
    fi

    if [[ ! -d "$abcli_path_git/$BLUER_JOURNAL_ASSETS" ]]; then
        abcli_log_error "@journal: repo not found, try running '@git clone $BLUER_JOURNAL_ASSETS' first."
        return 1
    fi

    return 0
}
