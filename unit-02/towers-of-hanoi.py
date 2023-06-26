#!/usr/bin/env python3

def print_move(fr, to):
    print(f"Moving from {fr} to {to}")

def move_tower(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
        return
    # print(n, fr, to, spare)
    move_tower(n - 1, fr, spare, to)
    move_tower(1, fr, to, spare)
    move_tower(n - 1, spare, to, fr)

move_tower(4, "P1", "P2", "P3")
