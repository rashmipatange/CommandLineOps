import pathlib
import click

@click.command()
#@click.argument('filename', type=click.File('r'))
@click.option('--path', prompt='Please enter path')

def main(path):
    #txt= filename.read()
    file=pathlib.Path(path)
    txt=file.read_text()
    click.echo(txt)
    vowels = "aeiuoAEIOU"
    count=len([letter for letter in txt if letter in vowels])

    click.echo('vowels count %s' %count)
if __name__=='__main__':
    main()
