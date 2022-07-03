# create followers
make builddb

http POST http://localhost:5001/friend fan_name=carina idol_name=ania
http POST http://localhost:5001/friend fan_name=roy idol_name=ania

# Create post
http POST http://localhost:5001/feed content="Ania loves fried chicken!" user_name=ania
http GET http://localhost:5001/timeline/roy
