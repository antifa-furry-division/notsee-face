# NotSee Face.

on the shoulders of giants

- [_IntelligenceX](https://twitter.com/_IntelligenceX/status/1346967229187952644)
- *and too many more to list*

# Usage

## Get the repo.

    https://github.com/antifa-furry-division/notsee-face.git

## Mirror The Data

Requires lftp [`apt-get install lftp`]

Run the mirror script.

    sh 00_mirror.sh
    
When it's done unzip the one zip.

`unzip Trump\ protest\ Jan\ 06\ 2021.zip`

## Normalize the File Names.

The filenames are a mess. 

This step:

1. Create a folder called `stage1` (mirroring the data being `stage2`)
1. Copy all .mp4 and .mkv files to `stage1/<md5sum>.<ext>`. (This doesn't need to be cryptographically secure, just unique)
 
