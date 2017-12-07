#!/bin/bash
socat TCP-LISTEN:23233,reuseaddr,fork EXEC:"./little_tommy"

