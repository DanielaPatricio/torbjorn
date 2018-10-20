source ~/virtual/environment/bin/activate; 
cd /home/empress/torbjorn; 
scrapy crawl productsspider2; 
cd /home/empress/Desktop; 
charcount=$(find -name "*product*" -printf '%f\n'| sort -nr | head -1 | xargs wc -c | awk '{print $1;}'); 
echo "$charcount";
linecount=$(find -name "*product*" -printf '%f\n'| sort -nr | head -1 | xargs wc -l | awk '{print $1;}'); 
echo "$linecount";
while [ $charcount = 0 ]; 
do sleep 30s;
source ~/virtual/environment/bin/activate; 
cd /home/empress/torbjorn; 
scrapy crawl productsspider2; 
cd /home/empress/Desktop; 
charcount=$(find -name "*product*" -printf '%f\n'| sort -nr | head -1 | xargs wc -c | awk '{print $1;}'); 
echo "$charcount";
linecount=$(find -name "*product*" -printf '%f\n'| sort -nr | head -1 | xargs wc -l | awk '{print $1;}'); 
((c++)) && ((c==10)) && break;
done;
if [ $charnum = 0 ]; 
then echo "Output file is empty" | mail -s "Script Error" daniela.santana.patricio@gmail.com;
else echo "Output file has $linecount items" | mail -s "Script Success" daniela.santana.patricio@gmail.com;
fi



