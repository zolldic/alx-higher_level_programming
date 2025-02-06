#!/bin/bash
cat "$1" | sudo mysql "$2"
