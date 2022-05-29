In this challenge we are presented with a file that has been corrupted in some way. Running 'file' command is not helpful as the output indicates that is just 'data'. Running 'strings' tool is more helpful as header strings we are able to discover are names of chunks from PNG header:

<p align="center"><img src="../../images/c0rrupt0.png" ></p>

Opening 'mystery' file in hexeditor lets us inspect the header more thoroughly.

<p align="center"><img src="../../images/c0rrupt1.png" ></p>

Looks like some knowledge about how PNG header works will be essential for this challenge. Decided to separate different parts with colors:

<p align="center"><img src="../../images/c0rrupt2.png" ></p>

Firstly, PNG file always starts with its' unique 8-byte PNG signature (purple color). After those 8 bytes, PNG header is divided into chunks. Every chunk contains 3 or 4 fields, depending whether chunk contains chunk data field. In our case every chunk contains 4 fields so that makes it a bit easier. 

a) First field is Data Length (yellow color) and length of this field = 4 bytes. This field described how many bytes are stored by Chunk Data field of this chunk. 

b) Second field (green color) contains Chunk Type and it's also a 4 byte value. If we translate every byte of this field, we get the name of the chunk.

c) Third field is Chunk Data (orange color). Length of this chunk varies and is described by first field (Data Length). Third field can contain 0 bytes but that does not happen in this challenge.

d) Last field (red color) is CRC (Cyclic Redundancy Code). Based on Chunk Type and Chunk Data fields, we calculate a checksum, that can be used to verify integrity of our chunk to see if nothing is corrupted.

So let's start with looking into first 8-byte (PNG signature)

<p align="center"><img src="../../images/c0rrupt3.png" ></p>

That means we have to fix byte #1 #3 #6 and #7:

<p align="center"><img src="../../images/c0rrupt4.png" ></p>

