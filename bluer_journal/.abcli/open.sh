#! /usr/bin/env bash

function bluer_journal_open() {
    local page=${1:-latest}

    [[ "$page" == "latest" ]] &&
        page=$(python3 -m bluer_journal.utils latest)

    if [[ "$INTERNET_IS_NATIONAL" == 1 ]]; then
        local filename=$abcli_path_git/$BLUER_JOURNAL_REPO.wiki
        [[ "$page" != "home" ]] &&
            filename=$filename/$page.md

        bluer_ai_code $filename
    else
        local url="https://github.com/kamangir/$BLUER_JOURNAL_REPO/wiki"
        [[ "$page" != "home" ]] &&
            url="$url/$page"

        bluer_ai_browse $url
    fi
}
