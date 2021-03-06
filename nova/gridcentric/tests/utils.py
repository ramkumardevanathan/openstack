# Copyright 2011 GridCentric Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova import db
from nova.compute import instance_types
from nova.compute import vm_states

def create_image(context, image={}):
    pass

def create_instance(context, instance={}):
        """Create a test instance"""

        instance.setdefault('user_id', 'fake')
        instance.setdefault('project_id', 'fake')
        instance.setdefault('instance_type_id', instance_types.get_instance_type_by_name('m1.tiny')['id'])
        instance.setdefault('image_id', 1)
        instance.setdefault('image_ref', 1)
        instance.setdefault('reservation_id', 'r-fakeres')
        instance.setdefault('launch_time', '10')
        instance.setdefault('mac_address', "ca:ca:ca:01")
        instance.setdefault('ami_launch_index', 0)
        instance.setdefault('vm_state', vm_states.ACTIVE)

        context.elevated()
        return db.instance_create(context, instance)['uuid']
