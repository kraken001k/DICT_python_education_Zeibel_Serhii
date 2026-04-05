import os
import sys
import hashlib
import shutil


VCS_DIR = 'vcs'
CONFIG = VCS_DIR + '/config.txt'      # username
INDEX = VCS_DIR  + '/index.txt'       # monitored files
LOG = VCS_DIR + '/log.txt'            # commit history
COMMITS_DIR = VCS_DIR + '/commits'    # directory with saves (commits)


commands = {
    'config': 'Make username.',
    'add': 'Add file',
    'commit': 'Commit changes',
    'log': 'Show log',
    'checkout': 'Return to one of the previous commits'
}


def init():
    """Creates the directory and file structure if they do not already exist."""
    os.makedirs(COMMITS_DIR, exist_ok=True)
    for file in [CONFIG, INDEX, LOG]:
        if not os.path.exists(file):
            open(file, 'w').close()


def read(path):
    """Read a line from a file (if the file is empty, return '')."""
    if not os.path.exists(path):
        return ''
    with open(path, 'r') as f:
        return f.read().strip()


def write(path, text):
    """Overwrites the file with the specified text."""
    with open(path, 'w') as f:
        f.write(text)


def append(path, text):
    """Appends text to the end of the file."""
    with open(path, 'a') as f:
        f.write(text)


def get_username():
    """Get username from config.txt"""
    return read(CONFIG)


def tracked_files():
    """Get a list of all files monitored by the system."""
    return read(INDEX).splitlines()


def file_hash(name):
    """SHA-1 hash of the file contents."""
    with open(name, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def changes():
    """
    Check for changes in tracked files since the last commit.
    Returns True if at least one file has changed.
    """
    if not os.path.getsize(LOG):
        return True
    files = tracked_files()
    last_commit = read(LOG).splitlines()[0].split()[1]
    for file in files:
        old_file = f'{COMMITS_DIR}/{last_commit}/{file}'
        if not os.path.exists(old_file) or file_hash(file) != file_hash(old_file):
            return True
    return False


def commit(message):
    """
    Creates a commit if there are changes and the username is specified.
    - calculates the total hash of the tracked files,
    - saves their copies in a separate folder (by hash),
    - writes a record to the log.
    """
    if not message:
        print('Nothing to commit')
        return
    if not changes():
        print('Nothing to commit')
        return
    username = get_username()
    if not username:
        print('Type your username')
        return
    files = tracked_files()
    total_hash = ''.join([file_hash(file) for file in files])
    commit_user_id = hashlib.sha1(total_hash.encode()).hexdigest()
    commit_path = f'{COMMITS_DIR}/{commit_user_id}'
    os.makedirs(commit_path)
    for file in files:
        shutil.copy(file, f'{commit_path}/{file}')
    log_entry = f'commit {commit_user_id}\nAuthor: {username}\n{message}\n\n'
    write(LOG, log_entry + read(LOG))
    print('Changes are saved')


def show_log():
    """Shows a list of all commits (if any)."""
    log_text = read(LOG)
    if log_text:
        print(log_text)
    else:
        "There are no logs"


def checkout(commit_user_id):
    """
    Replaces current files with those saved in the specified commit.
    """
    path = f'{COMMITS_DIR}/{commit_user_id}'
    if not os.path.exists(path):
        print('Commit not found')
        return
    for file in os.listdir(path):
        shutil.copy(f'{path}/{file}', file)
    print(f'Switched to commit {commit_user_id}')


def main():
    """The main handler of commands from command line arguments."""
    init()
    args = sys.argv[1:]
    if not args or args[0] == '--help':
        print('Here are commands:')
        for cmd, desc in commands.items():
            print(f'{cmd.ljust(10)}{desc}')
        return
    cmd = args[0]
    if cmd == 'config':
        if len(args) == 2:
            write(CONFIG, args[1])
            print(f'Username is {args[1]}')
        else:
            users_name = get_username()
            if users_name:
                print(users_name)
            else:
                print('Incorrect input!')
    elif cmd == 'add':
        if len(args) == 2:
            filename = args[1]
            if os.path.exists(filename):
                files = set(tracked_files())
                files.add(filename)
                write(INDEX, '\n'.join(files))
                print(f"There's {filename}")
            else:
                print(f"There's no {filename}")
        else:
            files = tracked_files()
            if files:
                print('Tracked files:')
                for file in files:
                    print(file)
            else:
                print('No files tracked.')
    elif cmd == 'commit':
        commit(args[1] if len(args) > 1 else '')
    elif cmd == 'log':
        show_log()
    elif cmd == 'checkout':
        if len(args) > 1:
            checkout(args[1])
        else:
            print('Type commit ID')
    else:
        print(f'{cmd} is unknown command')


if __name__ == '__main__':
    main()
