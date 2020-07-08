# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


from pyrobot.locobot.camera import LoCoBotCamera


class AzureKinectCamera(LoCoBotCamera):
    """
    This is camera class that interfaces with the Azure Kinect camera
    """

    def __init__(self, configs):
        """
        Constructor of the KinectV2Camera class.

        :param configs: Camera specific configuration object

        :type configs: YACS CfgNode
        """
        super(AzureKinectCamera, self).__init__(configs=configs)
