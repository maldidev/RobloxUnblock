#!/bin/bash
# THIS FILE IS NOT SAFE FOR USING AS NOT PROFFESIONAL!
echo "=== Universal Region Changer ==="
echo ""
echo "1. Set random region"
echo "2. Restore original"
echo "3. Show status"
echo "4. Exit"
echo ""

read -p "Select option (1-4): " choice

case $choice in
    1)
        ./region_linux.sh set
        ;;
    2)
        ./region_linux.sh restore
        ;;
    3)
        ./region_linux.sh status
        ;;
    4)
        exit 0
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

read -p "Press Enter to continue..."
