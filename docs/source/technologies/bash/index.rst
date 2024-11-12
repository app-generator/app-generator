:og:description: Getting Started with Bash - Learn the basics of Linux Scripting

Getting Started
===============

.. title:: Getting Started with Bash - Learn the basics of Linux Scripting    
.. meta::
    :description: Learn how to process files, list open ports, send alerts when disk is full .. etc

Bash (Bourne Again Shell) is a powerful command-line interface and scripting language that serves as the default shell for most Unix-based systems, including Linux distributions and macOS. 
It provides a comprehensive set of built-in commands, control structures, and features for text processing, file manipulation, and system administration tasks. 

.. include::  /_templates/components/banner-top.rst
    
Here are a few samples to get started with Bash. 

File Processing
---------------

Count lines, words, and characters in text files

.. code-block:: bash

    #!/bin/bash

    # Check if directory is provided
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <directory>"
        exit 1
    fi

    directory="$1"

    # Check if directory exists
    if [ ! -d "$directory" ]; then
        echo "Error: Directory not found"
        exit 1
    fi

    # Process text files
    for file in "$directory"/*.txt; do
        if [ -f "$file" ]; then
            echo "Processing: $file"
            wc "$file"
            echo "------------------------"
        fi
    done

List Open Ports
---------------

.. code-block:: bash

    #!/bin/bash

    echo "Open TCP ports:"
    netstat -tuln | grep LISTEN

    echo -e "\nOpen UDP ports:"
    netstat -uln

    # Alternative using ss command
    # echo "Open TCP ports:"
    # ss -tuln | grep LISTEN
    # 
    # echo -e "\nOpen UDP ports:"
    # ss -uln    

Disk Space Alert
----------------

.. code-block:: bash

    #!/bin/bash

    threshold=80
    email="admin@example.com"

    # Get disk usage percentage
    usage=$(df -h / | awk 'NR==2 {print $5}' | cut -d'%' -f1)

    if [ "$usage" -ge "$threshold" ]; then
        subject="Disk Space Alert: Usage at ${usage}%"
        message="Disk usage on $(hostname) has reached ${usage}%, exceeding the ${threshold}% threshold."
        
        echo "$message" | mail -s "$subject" "$email"
        echo "Alert sent: Disk usage is at ${usage}%"
    else
        echo "Disk usage is at ${usage}% - below threshold"
    fi

System Information Report
-------------------------

.. code-block:: bash

    #!/bin/bash

    echo "System Information Report"
    echo "========================="

    echo -e "\nHostname: $(hostname)"
    echo "Operating System: $(uname -s)"
    echo "Kernel Version: $(uname -r)"
    echo "Architecture: $(uname -m)"

    echo -e "\nCPU Information:"
    lscpu | grep "Model name" | sed 's/Model name:/CPU:/'

    echo -e "\nMemory Information:"
    free -h | awk '/^Mem:/ {print "Total: " $2 "\tUsed: " $3 "\tFree: " $4}'

    echo -e "\nDisk Usage:"
    df -h / | awk 'NR==2 {print "Total: " $2 "\tUsed: " $3 "\tAvailable: " $4 "\tUse%: " $5}'

    echo -e "\nCurrent Users:"
    who

    echo -e "\nTop 5 Processes by CPU Usage:"
    ps aux --sort=-%cpu | head -n 6

    echo -e "\nNetwork Interfaces:"
    ip addr | awk '/^[0-9]:/ {print $2}' | sed 's/://'    


Log File Analysis
-----------------

.. code-block:: bash

    #!/bin/bash

    log_file="/var/log/apache2/access.log"
    num_lines=10

    if [ ! -f "$log_file" ]; then
        echo "Error: Log file not found"
        exit 1
    fi

    echo "Top $num_lines IP addresses:"
    awk '{print $1}' "$log_file" | sort | uniq -c | sort -nr | head -n "$num_lines"

    echo -e "\nTop $num_lines requested pages:"
    awk '{print $7}' "$log_file" | sort | uniq -c | sort -nr | head -n "$num_lines"

    echo -e "\nHTTP status code distribution:"
    awk '{print $9}' "$log_file" | sort | uniq -c | sort -nr

    echo -e "\nTop $num_lines user agents:"
    awk -F'"' '{print $6}' "$log_file" | sort | uniq -c | sort -nr | head -n "$num_lines"

    echo -e "\nRequests per hour:"
    awk '{print $4}' "$log_file" | cut -d: -f2 | sort | uniq -c | sort -n

These scripts demonstrate various Bash features and common system administration tasks. Remember to make the scripts executable using `chmod +x script_name.sh` before running them.

As you continue learning Bash, focus on understanding control structures, variable manipulation, command substitution, and file operations. 
Practice writing scripts to automate tasks you frequently perform manually. Also, familiarize yourself with common Unix commands and utilities, as they are often used in Bash scripts.

.. include::  /_templates/components/footer-links.rst
