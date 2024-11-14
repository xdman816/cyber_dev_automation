#!/bin/bash

# watch for created files (new downloads) 
watch_folder="/mnt/test_folder"

temp_extensions="part crdownload download" #these are some of the common temp extensions

inotifywait -m -r -e create "$watch_folder" | while read -r dir action file; do
    if [ "$action" = "CREATE" ]; then
       # path to file
        new_file="$dir/$file"

        # Temporary file extensiion handling 
        while true; do
            # Get the file extension
            file_ext="${file##*.}"
            
            # Check if the file has a temporary extension
            if [[ "$temp_extensions" == *"$file_ext"* ]]; then
                echo "File is still downloading or has a temporary extension: $file"
                sleep 5  # Wait 5 seconds before checking again
            else
                # File doesn't have a temporary extension, so it's likely done
                break
            fi
        done

        # Now output the sha256sum of file
        hash=$(sha256sum "$new_file" | awk '{ print $1 }')

        # pass the hash into virust total script 
        python3 virustotal_search.py "$hash"
    fi
done

