# crpyt
`crpyt` is a tool to encrypt and decrypt media files preserving the media type.
For example, it can encrypt the content of image files such as JPEG images and the resulting file is still identified as an image file but it can no longer be viewed.
 
## Usage

`crpyt` can be used as follows to encrypt a file or folder:

```
crpyt [input file or folder]
```

Similarly, the following command is used to decrypt a file or folder:

```
crpyt --decrypt [input file or folder]
```

By default, the output will be written to the same folder where the input is found with the suffix `crpyt`:
- If the input is a folder with name `[folder_name]`, the output can be found in the folder `[folder_name]_crpyt`.
- If the input is a file with name `[file_name].[extension]`, the ouput is called `[file_name]_crpyt.[extension]`.

Optional arguments can be provided to change the behavior of `crpyt`. All possible arguments can be viewed by executing the following command:

```
crpyt --help
```
