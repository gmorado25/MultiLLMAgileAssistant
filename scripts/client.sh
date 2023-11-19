cd $1
cd client

if [ $(NEXTJS_DEBUG) == "True"]; then
    npx next dev -H $(NEXTJS_ADDRESS) -p $(NEXTJS_PORT)
else
    npx next build
    npx next start -H $(NEXTJS_ADDRESS) -p $(NEXTJS_PORT)
fi
read -n1 -r -p "Press any key to continue..." key
