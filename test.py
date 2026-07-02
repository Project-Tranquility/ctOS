#!/usr/bin/env python3
import time
import random
from collections import deque
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich.panel import Panel

console = Console()
GREEN = "bold spring_green2"
DIM_GREEN = "spring_green4"

BOOT_LINES = [
    "[INIT] Loading all module...",
    "[NET ] Establishing uplink to backbone...",
    "[OK  ] All systems are onlines.",
]

SPACE_LINE = [
    " "
]

WAITING_LINE = [
    "."
    ".."
    "..."
]

START_LINE = [
    "Hello from cpOS"
]

def make_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="main", ratio=2),
        Layout(name="bottom", size=9),
    )
    layout["bottom"].split_row(
        Layout(name="bottom_left"),
    )
    return layout

def render_center(percent: int, width: int = 40) -> Align:
    filled = int(width * percent / 100)
    empty = width - filled
    bar_str = "█" * filled + "░" * empty
    text = Text(f"{bar_str} {percent:3d}%", style=GREEN, justify="center")
    return Align.center(text, vertical="middle")

def render_status(history: deque) -> Panel:
    body = Text("\n".join(history), style=DIM_GREEN)
    return Panel(body, border_style=DIM_GREEN)

def demo():
    layout = make_layout()
    history = deque(maxlen=6)
    messages = BOOT_LINES
    start = START_LINE
    wait = WAITING_LINE
    nb_task = 0
    i = 0
    is_finish = False
    

    with Live(layout, console=console, refresh_per_second=20, screen=True):
        while is_finish is False:
            i = i + 1
            percent = (i * 100 // 59)
            layout["main"].update(render_center(percent))

            if i % 5 == 0:
                history.append(random.choice(messages) + f" {random.randint(0,99)}%")
                nb_task = nb_task + 1
            layout["bottom_left"].update(render_status(history))

            if (percent >= 100):
                is_finish = True
            time.sleep(0.08)


if __name__ == "__main__":
    demo()