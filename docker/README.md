
rsync -vaz --rsync-path="sudo rsync" --no-perms --no-owner --no-group --exclude '.git src/fe_eng/node_modules' . vunm@10.5.22.7:/home/vunm/eng


docker-compose up -d --build frontend