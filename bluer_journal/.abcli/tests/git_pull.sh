#! /usr/bin/env bash

function test_bluer_journal_git_pull() {
    if [[ "$BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE" == 0 ]]; then
        bluer_ai_log_warning "outside is not accessible, test is disabled."
        return
    fi

    local options=$1

    bluer_journal_git_pull
}
