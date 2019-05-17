# ping tool

Use this tool to monitor your latency to a secified hostname.

This package includes two basic tools
NOTE: Please cd into the directory to use it properly.

1. ping-tool.py [hostname]

    This tool stores the latency to a non-formatted file.
    NOTE: this tool requires root privilieges to work
    EXAMPLE:        sudo python ping-tool.py google.com
    
2. fetch_results.py
    
    This tool returns the data in JSON and saves it to the file "pingresults.txt" in the tools directory.
    EXAMPLE:        python fetch_results.py
    
    
    Copyright by Leon Mitteldorf
