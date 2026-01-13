#! /usr/bin/env bash

function bluer_journal_next() {
    local page=$(python3 -m bluer_journal.utils get --what next)
    page=${1:-$page}

    python3 -m bluer_journal.utils \
        create_next_page \
        --page $page
    [[ $? -ne 0 ]] && return 1

    local options=$2
    local do_open=$(bluer_ai_option_int "$options" open 1)
    if [[ "$do_open" == 1 ]]; then
        bluer_journal_open $page
    fi
}
