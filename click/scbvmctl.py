import click

@click.group()
def vmcli():
    pass

@vmcli.command()
def create():
    """Create Virtual Machine"""

@click.group()
def snapshot():
    pass

@snapshot.command()
def create():
    """Create VM snapshot"""

scbvmctl = click.CommandCollection(sources=[vmcli, snapshot])

if __name__ == '__main__':
    scbvmctl()