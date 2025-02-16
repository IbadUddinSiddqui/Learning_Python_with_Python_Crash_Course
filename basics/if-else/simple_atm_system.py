from rich.console import Console

console = Console()
balance = 2000
pin = 4500
attempts = 3

while attempts > 0:
    PIN = int(console.input("[bold green]Enter Your pin:....[/bold green] "))
    
    if pin == PIN:
        while True:
            address = str(console.input("[yellow]Type 'Balance' for checking balance or 'Withdraw' for getting cash:.....[/yellow] "))
            if address.lower() == "balance":
                console.print(f'[bold green]Your balance is {balance}[/bold red]')
                break
            elif address.lower() == "withdraw":
                if balance > 0:
                    amount = int(console.input("[blue]Enter Amount:.....[/blue] "))
                    if amount <= balance:
                        balance -= amount
                        console.print(f'[bold underline green]Transaction Successful and remaining amount is {balance}[bold underline green]')
                    else:
                        console.print("[bold underline red]Insufficient Balance[/bold underline red]")
                    break
                else:
                    console.print("[bold underline red]Insufficient Balance[/bold underline red]")
                    break
            else:
                console.print("[bold underline red]Invalid option. Please type 'Balance' or 'Withdraw'[/bold underline red]")
        break  
    else:
        attempts -= 1
        if attempts > 0:
            console.print(f"[bold underline blue]Wrong PIN. You have {attempts} attempts remaining[/bold underline blue]")
        else:
            print("[bold underline yellow]Too many wrong tries\nSession Logged Out[/bold underline yellow]")