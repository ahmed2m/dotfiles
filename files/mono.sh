#!/bin/bash

NUMBER=$(pacmd list-sinks | grep name: | wc -l)
echo "Getting $NUMBER audio interface"
sinks=()

for ((c = 1; c <= $NUMBER; c++)); do
    SINK=$(pacmd list-sinks | grep name: | sed -n ${c}p)
    # One liner to extract the sink string from `stackoverflow`
    # $sink_string = pacmd list-sinks | grep -m 1 -oP 'name:\s<\K.*(?=>)' | head $d
    sink_string=$(echo "$SINK" | cut -d "<" -f2 | cut -d ">" -f1)
    echo "Getting Audio Interface:  $sink_string"
    if [[ $sink_string == "mono-"* ]]; then
        echo -e "\t Removing old mono interface."
        continue
    fi

    sinks+=("$sink_string")
done

# remove old mono channels
$(pactl unload-module module-remap-sink)

for sink in "${sinks[@]}"; do
    echo -e "Adding mono sink for $sink\n"
    $(pacmd load-module module-remap-sink sink_name=mono-$sink master=$sink channels=2 channel_map=mono,mono)
done
