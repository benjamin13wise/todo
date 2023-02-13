import click
@click.group
def mycommands():
    pass


priorities = {
    'o' : 'optional',
    'l' : 'low',
    'm' : 'medium',
    'h' : 'high',
    'c' : 'crucial',
}

@click.command()
@click.argument("priority",type = click.Choice(priorities.keys()),default ='m')
@click.option('-n','--name',prompt = 'Enter the to do name: ',help ='The name of the to do item')
@click.option('-d','--desc',prompt = 'Describe the to do: ',help ='Describe the to do item')
def addToDo(name,desc,priority):
    filename =  'mytodos.txt'
    with open (filename, 'a+') as f:
        f.write(f"{name}: {desc} [priority:{priorities[priority]}]\n")
    
@click.command()
@click.argument('idx',type = int,required = 1)
def deleteToDo(idx):
    with open("mytodos.txt", 'r') as f:
        toDoList = f.read().splitlines()
        toDoList.pop(idx)
    with open("mytodos.txt", 'w') as f:
        f.write("\n".join(toDoList))
        f.write("\n")

@click.command()
@click.option('-p','--priority',type = click.Choice(priorities.keys()))
def showToDo(priority):
    filename = 'mytodos.txt'
    with open(filename,'r') as f:
        toDoList = f.read().splitlines()
    if priority is None:
        for idx , toDo in enumerate(toDoList):
            print(f"{idx} - {toDo}")
    else:
        for idx , toDo in enumerate(toDoList):
            if f"[priority : {priorities[priority]}]" in toDo:
                print(f"{idx} - {toDo}")


mycommands.add_command(addToDo)
mycommands.add_command(deleteToDo)
mycommands.add_command(showToDo)


if __name__ == "__main__":
    mycommands()
