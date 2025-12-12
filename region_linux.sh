#!/bin/bash
# Use sudo or doas for using it.
echo "Region Changer for Linux"
echo ""

if [ "$1" = "set" ]; then
    echo "Setting random region..."
    sudo python3 region_manager.py set
elif [ "$1" = "restore" ]; then
    echo "Restoring original settings..."
    sudo python3 region_manager.py restore
elif [ "$1" = "status" ]; then
    echo "Current status:"
    python3 region_manager.py status
else
    echo "Usage: $0 [set|restore|status]"
    echo ""
    echo "  set     - Set random region"
    echo "  restore - Restore original"
    echo "  status  - Show current"
fi
