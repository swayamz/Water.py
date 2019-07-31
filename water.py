import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import psycopg2

CLK  = 12
MISO = 16
MOSI = 20
CS   = 21
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


while True:
    con = psycopg2.connect(
            host = "raja.db.elephantsql.com",
            database = "xwcksumk",
            user = "xwcksumk",
            password = "MhkCwNz7hBjt7bg5cuq5KUdkV9ILaPV2",
            port = "5432"
    )
    cur = con.cursor()
    values = [0]*8
    for i in range(8):
        values[i] = round(mcp.read_adc(i)/10.24)
    print(values)
    myTime = time.strftime("%d %b %Y %H:%M:%S")
    cur.execute('INSERT INTO calc_farmdata (time, x, y, value) VALUES (%s, %s, %s, %s)', (myTime, "A", "v1", values[0]))
    cur.execute('INSERT INTO calc_farmdata (time, x, y, value) VALUES (%s, %s, %s, %s)', (myTime, "A", "v2", values[1]))
    cur.execute('INSERT INTO calc_farmdata (time, x, y, value) VALUES (%s, %s, %s, %s)', (myTime, "B", "v1", values[2]))
    cur.execute('INSERT INTO calc_farmdata (time, x, y, value) VALUES (%s, %s, %s, %s)', (myTime, "B", "v2", values[3]))
    cur.execute('INSERT INTO calc_farmdata (time, x, y, value) VALUES (%s, %s, %s, %s)', (myTime, "C", "v1", values[4]))
    con.commit()
    cur.close()
    con.close()
    time.sleep(10)