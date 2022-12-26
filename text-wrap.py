import textwrap

def wrap(string, max_width):
    wrapper = textwrap.wrap(string, max_width)
    return '\n'.join(wrapper)

if __name__ == '__main__':
