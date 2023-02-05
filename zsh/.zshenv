wall=('bladerunner.jpg' 'cape.jpg' 'delorean.jpg' 'knight.jpg' 'legion.jpg' 'marx.jpg' 'witcher.jpg' 'xiaohong.jpg')
export WALL=$wall[$((RANDOM % ${#wall[@]}))+1]
