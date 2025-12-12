#!/bin/bash

echo "Installing Region Changer..."
echo ""
echo "Copying files..."
mkdir -p ~/bin
cp region_manager.py ~/bin/
cp region_linux.sh ~/bin/
cp run_region.sh ~/bin/
chmod +x ~/bin/region_linux.sh ~/bin/run_region.sh
echo ""
echo "Adding to PATH..."
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
echo ""
echo "Installation complete!"
echo "Restart terminal or run: source ~/.bashrc"