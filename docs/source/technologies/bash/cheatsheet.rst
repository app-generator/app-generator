Cheatsheet
==========

Bash (Bourne Again Shell) is the default command-line interpreter for most Linux distributions and macOS. 
Created by Brian Fox in 1989 as a free replacement for the Bourne Shell, Bash has become the de facto standard for shell scripting. 
It's both a command interpreter and a programming language, allowing users to automate tasks and create powerful scripts.

.. include::  /_templates/components/banner-top.rst

**Advanced File Operations**

.. code-block:: bash    

    # Find and process files
    find . -type f -name "*.log" -mtime +30 -exec rm {} \;

    # Mass rename files
    for f in *.jpeg; do 
        mv "$f" "${f%.jpeg}.jpg"
    done

    # Create directory structure with parents
    mkdir -p project/{src,docs,tests}/{main,utils}

    # Secure file deletion
    shred -u -z -n 3 sensitive_file.txt
        
**Process Management**

.. code-block:: bash    

    # Run command in background and save output
    nohup long_running_script.sh > output.log 2>&1 &

    # Get process ID of last background command
    echo $!

    # Kill all processes matching pattern
    pkill -f "python.*myapp"

    # Monitor process resource usage
    top -p $(pgrep -d',' python)
        

**String Manipulation**

.. code-block:: bash    

    string="Hello World"

    # Substring extraction
    echo ${string:6:5}  # "World"

    # String replacement
    echo ${string//o/0}  # "Hell0 W0rld"

    # Convert to uppercase/lowercase
    echo ${string^^}  # "HELLO WORLD"
    echo ${string,,}  # "hello world"

    # Strip prefix/suffix
    filename="script.sh.bak"
    echo ${filename%.bak}  # "script.sh"
        

**Array Operations**

.. code-block:: bash    

    # Declare array
    declare -a fruits=("apple" "banana" "orange")

    # Add element
    fruits+=("mango")

    # Get length
    echo ${#fruits[@]}

    # Slice array
    echo ${fruits[@]:1:2}

    # Associative array (hash/dictionary)
    declare -A config
    config[host]="localhost"
    config[port]="8080"

        
**Error Handling and Debugging**

.. code-block:: bash    

    # Enable debugging
    set -x  # Print commands
    set -e  # Exit on error
    set -u  # Error on undefined variables

    # Error handling function
    handle_error() {
        echo "Error on line $1"
        exit 1
    }
    trap 'handle_error $LINENO' ERR

    # Conditional error checking
    command || { echo "Command failed"; exit 1; }
        

**Advanced Input/Output**

.. code-block:: bash    

    # Read file line by line
    while IFS= read -r line; do
        echo "Processing: $line"
    done < input.txt

    # Here document
    cat << EOF > config.yml
    server:
    port: 8080
    host: localhost
    EOF

    # Process substitution
    diff <(sort file1.txt) <(sort file2.txt)
        
        
**Network Operations**

.. code-block:: bash    

    # Check if port is open
    nc -zv localhost 80

    # Simple HTTP server
    while true; do
        echo -e "HTTP/1.1 200 OK\n\nHello" | nc -l 8080
    done

    # Download with progress
    wget --progress=bar:force -O output.file url

    # Monitor network connections
    watch -n 1 'netstat -tuln'
        

**Date and Time Operations**

.. code-block:: bash    

    # CONTENT_HERE


**SECTION**

.. code-block:: bash    

    # Format current date
    now=$(date +"%Y-%m-%d_%H-%M-%S")

    # Date arithmetic
    tomorrow=$(date -d "tomorrow" +%Y-%m-%d)
    last_week=$(date -d "7 days ago" +%Y-%m-%d)

    # Create timestamp for files
    touch -t 202312311200.00 file.txt

    # Measure execution time
    SECONDS=0
    sleep 5
    echo "Operation took $SECONDS seconds"

        
**Security and Permissions**

.. code-block:: bash    

    # Set secure permissions
    chmod 750 script.sh
    umask 027

    # Generate random password
    openssl rand -base64 32

    # Calculate file hash
    sha256sum file.txt

    # Find SUID files
    find / -perm /4000 -type f 2>/dev/null


**Advanced Script Features**

.. code-block:: bash    

    # Getopts for argument parsing
    while getopts ":h:p:v" opt; do
        case $opt in
            h) host="$OPTARG";;
            p) port="$OPTARG";;
            v) verbose=1;;
            \?) echo "Invalid option: -$OPTARG";;
        esac
    done

    # Function with return value
    is_number() {
        [[ $1 =~ ^[0-9]+$ ]]
        return $?
    }

    # Lock file to prevent multiple instances
    LOCKFILE="/tmp/script.lock"
    if ! mkdir "$LOCKFILE" 2>/dev/null; then
        echo "Script is already running"
        exit 1
    fi
    trap 'rm -rf "$LOCKFILE"' EXIT
    
            
**PRO Tips**

- Use set -euo pipefail for safer scripts
- Always quote variables: "$variable"
- Use shellcheck for script validation
- Use $(command) instead of backticks
- Learn to use man pages effectively
- Use ctrl+r for history search
- Create aliases for common commands
- Use screen or tmux for persistent sessions
- Master regex patterns for text processing
- Keep scripts modular and documented


.. include::  /_templates/components/footer-links.rst
