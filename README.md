# NotSee Face.

on the shoulders of giants

- [_IntelligenceX](https://twitter.com/_IntelligenceX/status/1346967229187952644)
- *and too many more to list*

# Usage

## Get the repo.

    https://github.com/antifa-furry-division/notsee-face.git
    
## Setup Python
 
    python3 -mvenv venv
    source venv/bin/activate
    pip install -U pip wheel setuptools
    pip install -r requirements.txt

## Mirror The Data

Requires lftp [`apt-get install lftp`]

Run the mirror script.

    sh 00_mirror.sh
    
When it's done unzip the one zip.

`unzip Trump\ protest\ Jan\ 06\ 2021.zip`

## Normalize the File Names.

This step:

1. Creates a folder called `stage1` (mirroring the data being `stage2`)
1. Copies all .mp4 and .mkv files to `stage1/<md5sum>.<ext>`. (This doesn't need to be cryptographically secure, just unique)

Justification: The filenames are all over the place. Filenames are the same size, you can usually specify a file by the first 3-4 digits alone, flat folder structure.
 
## Batch extract 

[Setting up `face_recognition` with CUDA is out of scope of this tutorial]

1. Copy `batch_face_extract.py` into `stage1` and run it.
1. Run `batch_face_extract.py`, #walkaway

Creates:

- Folder `<video>_faces/`
- Images of faces: `<video>_faces/<video>_0000000.jpg`
  

## Annotate Video

Show off to your friends and family that went how easy it is to outline a face in 2021.

https://www.youtube.com/watch?v=p7XBr1GTAmo&feature=youtu.be

    python3 extract_facesv2.py <video.mp4>
   
Creates: `<video>_faces.mp4`


## Extract faces v2.

Uses a different algorithm, works on 1 video at a time.

    python3 extract_facesv2.py <video.mp4>
   
Creates:

- Folder `<video>_faces/`
- Images of faces: `<video>_faces/<video>_0000000.jpg`
   
# Digital Forensics XML

[capitol.dfxml](https://github.com/antifa-furry-division/notsee-face/blob/main/capitol.dfxml)

Digital Forensics XML is an XML language used to automate digital forensics processing. DFXML contains information about both the results of forensic processing and the tools used to perform the processing. Currently there is no Digital Forensics XML standard and there is no fixed schema. There is a draft schema available from NIST.

- https://github.com/simsong/dfxml/
- https://en.wikipedia.org/wiki/Digital_Forensics_XML
