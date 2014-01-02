#!/bin/bash
WORKSPACES=$(gsettings get org.mate.Marco.general num-workspaces)
echo "currently $WORKSPACES workspaces"
echo "Removing one, so now there will be $(( WORKSPACES - 1 ))"
gsettings set org.mate.Marco.general num-workspaces $(( WORKSPACES - 1))
