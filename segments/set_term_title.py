def add_set_term_title_segment(powerline):
    term = os.getenv('TERM')
    if not (('xterm' in term) or ('rxvt' in term)):
        return

    if powerline.args.shell == 'bash':
        title = os.getenv('TITLE', '\\u@\\h: \\w')
        set_title = '\\[\\e]0;{0}\\a\\]'.format(title)
    elif powerline.args.shell == 'zsh':
        title = os.getenv('TITLE', '%n@%m: %~')
        set_title = '\033]0;{0}\007'.format(title)
    else:
        import socket
        set_title = '\033]0;%s@%s: %s\007' % (os.getenv('USER'), socket.gethostname().split('.')[0], powerline.cwd or os.getenv('PWD'))

    powerline.append(set_title, None, None, '')

