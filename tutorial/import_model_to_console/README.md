# Import PoseNet model to **Console for AITRIOS**

This directory provides a Jupyter Notebook to import PoseNet model used for keypoint detection to **Console for AITRIOS**. <br>
By running the [import_model_to_console.ipynb](./import_model_to_console.ipynb), you can import the AI model into the **Console** by using **Console REST API** and you are ready to deploy it to the device.

> **NOTE**
>
> If you want to import an AI model with using **Console UI**, see [**Console User Manual**](https://developer.aitrios.sony-semicon.com/en/edge-ai-sensing/documents/console-user-manual/) for details.

## Overview

To prepare an AI model for deploying it to the device, the following steps need to be taken. <br>
The [import_model_to_console.ipynb](./import_model_to_console.ipynb) provides a code-based way to perform these steps.

1. Get model in **`tflite`** format by downloding it.
2. Upload model file from local by using **UploadFile API**.
3. Import uploaded model file above to **Console for AITRIOS** as a base AI model, by using **ImportBaseModel API**.
4. Convert imported model above into a form that can be executed on the device, by using **PublishModel API**.

## Get Started

### 1. Get PoseNet model

Download the PoseNet model **`./posenet_mobilenet_v1_075_353_481_quant.tflite`** from the [Google Coral repository](https://github.com/google-coral/project-posenet/blob/master/models/mobilenet/components/posenet_mobilenet_v1_075_353_481_quant.tflite) and place it.
(Other AI models has not been verified.)

### 2. Create import setting file

Place setting file (**`./configuration.json`** file) for importing.

- configuration.json
  
    ```json
        {
            "model_id": "",
            "model_file_id": "",
            "converted": false,
            "vendor_name": "",
            "comment": "",
            "network_type": "0",
            "labels": []
        }
    ```

- configuration.json (example without optional parameters)

    ```json
        {
            "model_id": ""
        }
    ```

### 3. Edit settings

Edit the parameters in [configuration.json](./configuration.json).

The parameters required to run this notebook are :
|Setting|Description|Range|Required/Optional|Remarks
|:--|:--|:--|:--|:--|
|**`model_id`**|The ID of the AI model you want to import|String. <br>See NOTE. |Required|Used for "**Console REST API**":<br> **`ImportBaseModel`**|
|**`model_file_id`**|Unique file ID derived from Console|String. <br>See NOTE. |Not in use|Used for "**Console REST API**":<br> **`ImportBaseModel`**<br> Leave blank as it will be automatically filled in.|
|**`converted`**|AI model converted flag <br>If set to false, the model will be converted at import on "**Console for AITRIOS**" |true or false. <br> (typical: false) <br>See NOTE. |Optional|Used for "**Console REST API**":<br> **`ImportBaseModel`**|
|**`vendor_name`**|vendor name|String. <br>See NOTE. |Optional|Used for "**Console REST API**":<br> **`ImportBaseModel`**|
|**`comment`**|Description of the AI model and version|String. <br>See NOTE. |Optional|Used for "**Console REST API**":<br> **`ImportBaseModel`**|
|**`network_type`**|network type|String. <br>See NOTE. |Optional<br>If omitted, set default value:"0"  *1|Used for "**Console REST API**":<br> **`ImportBaseModel`**|
|**`labels`**|Label names|["label01", "label02", ...]<br>See NOTE. |Optional|Used for "**Console REST API**":<br> **`ImportBaseModel`**|

> **NOTE**<br>
> See [Console REST API reference](https://developer.aitrios.sony-semicon.com/en/edge-ai-sensing/guides/) for other restrictions.

### 4. Create Console access configuration file

Create console access setting configuration file with real values in **`console_access_settings.yaml`**. Please refer to the [README](../../README.md#start-application-on-github-codespaces) in this repository for details.

### 4. Run the notebook

Open [notebook](./import_model_to_console.ipynb) and run the cells.

You can run all cells at once, or you can run the cells one by one.

If successful, AI model will be imported to and converted in the "**Console for AITRIOS**" and the following log will be displayed:

```bash
Converting... 
 model_id: xxxxxxxxx
```

Converting AI model will take some time, so run the "Get AI model status after conversion" cell to check the result of conversion.

When the "Get AI model status after conversion" cell is executed, the conversion status of each device is displayed as follows:

```bash
Conversion completed 
 model_id: xxxxxxxxx
```

The status is "Converting...", "Conversion completed", "Conversion failed".

## 
