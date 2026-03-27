from kagglesdk.kaggle_object import *
from typing import Optional

class KernelSessionInfo(KaggleObject):
  r"""
  This class is serialized to XML and saved in the KernelSessions table's
  IsolatorResults column. If you make a change (add a field, remove a field)
  here, also change the serializer/deserializer in
  'Kaggle.Service.Kernels/Utils/IsolatorResults.cs'.

  Attributes:
    dockerfile_url (str)
    docker_hub_url (str)
      This url now points to Google Container Registry (gcr.io).
    docker_image_digest (str)
    docker_image_id (str)
    docker_image_name (str)
    disk_kb_free (int)
    failure_message (str)
    exit_code (int)
    queued_seconds (int)
    output_size_bytes (int)
    run_time_seconds (float)
    used_all_space (bool)
    timeout_exceeded (bool)
    is_valid_status (bool)
    was_gpu_enabled (bool)
    was_internet_enabled (bool)
    out_of_memory (bool)
    invalid_path_errors (bool)
    succeeded (bool)
    was_killed (bool)
  """

  def __init__(self):
    self._dockerfile_url = None
    self._docker_hub_url = None
    self._docker_image_digest = None
    self._docker_image_id = None
    self._docker_image_name = None
    self._disk_kb_free = None
    self._failure_message = None
    self._exit_code = 0
    self._queued_seconds = None
    self._output_size_bytes = None
    self._run_time_seconds = 0.0
    self._used_all_space = False
    self._timeout_exceeded = False
    self._is_valid_status = None
    self._was_gpu_enabled = None
    self._was_internet_enabled = None
    self._out_of_memory = False
    self._invalid_path_errors = False
    self._succeeded = False
    self._was_killed = False
    self._freeze()

  @property
  def dockerfile_url(self) -> str:
    return self._dockerfile_url or ""

  @dockerfile_url.setter
  def dockerfile_url(self, dockerfile_url: Optional[str]):
    if dockerfile_url is None:
      del self.dockerfile_url
      return
    if not isinstance(dockerfile_url, str):
      raise TypeError('dockerfile_url must be of type str')
    self._dockerfile_url = dockerfile_url

  @property
  def docker_hub_url(self) -> str:
    """This url now points to Google Container Registry (gcr.io)."""
    return self._docker_hub_url or ""

  @docker_hub_url.setter
  def docker_hub_url(self, docker_hub_url: Optional[str]):
    if docker_hub_url is None:
      del self.docker_hub_url
      return
    if not isinstance(docker_hub_url, str):
      raise TypeError('docker_hub_url must be of type str')
    self._docker_hub_url = docker_hub_url

  @property
  def docker_image_digest(self) -> str:
    return self._docker_image_digest or ""

  @docker_image_digest.setter
  def docker_image_digest(self, docker_image_digest: Optional[str]):
    if docker_image_digest is None:
      del self.docker_image_digest
      return
    if not isinstance(docker_image_digest, str):
      raise TypeError('docker_image_digest must be of type str')
    self._docker_image_digest = docker_image_digest

  @property
  def docker_image_id(self) -> str:
    return self._docker_image_id or ""

  @docker_image_id.setter
  def docker_image_id(self, docker_image_id: Optional[str]):
    if docker_image_id is None:
      del self.docker_image_id
      return
    if not isinstance(docker_image_id, str):
      raise TypeError('docker_image_id must be of type str')
    self._docker_image_id = docker_image_id

  @property
  def docker_image_name(self) -> str:
    return self._docker_image_name or ""

  @docker_image_name.setter
  def docker_image_name(self, docker_image_name: Optional[str]):
    if docker_image_name is None:
      del self.docker_image_name
      return
    if not isinstance(docker_image_name, str):
      raise TypeError('docker_image_name must be of type str')
    self._docker_image_name = docker_image_name

  @property
  def disk_kb_free(self) -> int:
    return self._disk_kb_free or 0

  @disk_kb_free.setter
  def disk_kb_free(self, disk_kb_free: Optional[int]):
    if disk_kb_free is None:
      del self.disk_kb_free
      return
    if not isinstance(disk_kb_free, int):
      raise TypeError('disk_kb_free must be of type int')
    self._disk_kb_free = disk_kb_free

  @property
  def failure_message(self) -> str:
    return self._failure_message or ""

  @failure_message.setter
  def failure_message(self, failure_message: Optional[str]):
    if failure_message is None:
      del self.failure_message
      return
    if not isinstance(failure_message, str):
      raise TypeError('failure_message must be of type str')
    self._failure_message = failure_message

  @property
  def exit_code(self) -> int:
    return self._exit_code

  @exit_code.setter
  def exit_code(self, exit_code: int):
    if exit_code is None:
      del self.exit_code
      return
    if not isinstance(exit_code, int):
      raise TypeError('exit_code must be of type int')
    self._exit_code = exit_code

  @property
  def queued_seconds(self) -> int:
    return self._queued_seconds or 0

  @queued_seconds.setter
  def queued_seconds(self, queued_seconds: Optional[int]):
    if queued_seconds is None:
      del self.queued_seconds
      return
    if not isinstance(queued_seconds, int):
      raise TypeError('queued_seconds must be of type int')
    self._queued_seconds = queued_seconds

  @property
  def output_size_bytes(self) -> int:
    return self._output_size_bytes or 0

  @output_size_bytes.setter
  def output_size_bytes(self, output_size_bytes: Optional[int]):
    if output_size_bytes is None:
      del self.output_size_bytes
      return
    if not isinstance(output_size_bytes, int):
      raise TypeError('output_size_bytes must be of type int')
    self._output_size_bytes = output_size_bytes

  @property
  def run_time_seconds(self) -> float:
    return self._run_time_seconds

  @run_time_seconds.setter
  def run_time_seconds(self, run_time_seconds: float):
    if run_time_seconds is None:
      del self.run_time_seconds
      return
    if not isinstance(run_time_seconds, float):
      raise TypeError('run_time_seconds must be of type float')
    self._run_time_seconds = run_time_seconds

  @property
  def used_all_space(self) -> bool:
    return self._used_all_space

  @used_all_space.setter
  def used_all_space(self, used_all_space: bool):
    if used_all_space is None:
      del self.used_all_space
      return
    if not isinstance(used_all_space, bool):
      raise TypeError('used_all_space must be of type bool')
    self._used_all_space = used_all_space

  @property
  def timeout_exceeded(self) -> bool:
    return self._timeout_exceeded

  @timeout_exceeded.setter
  def timeout_exceeded(self, timeout_exceeded: bool):
    if timeout_exceeded is None:
      del self.timeout_exceeded
      return
    if not isinstance(timeout_exceeded, bool):
      raise TypeError('timeout_exceeded must be of type bool')
    self._timeout_exceeded = timeout_exceeded

  @property
  def is_valid_status(self) -> bool:
    return self._is_valid_status or False

  @is_valid_status.setter
  def is_valid_status(self, is_valid_status: Optional[bool]):
    if is_valid_status is None:
      del self.is_valid_status
      return
    if not isinstance(is_valid_status, bool):
      raise TypeError('is_valid_status must be of type bool')
    self._is_valid_status = is_valid_status

  @property
  def was_gpu_enabled(self) -> bool:
    return self._was_gpu_enabled or False

  @was_gpu_enabled.setter
  def was_gpu_enabled(self, was_gpu_enabled: Optional[bool]):
    if was_gpu_enabled is None:
      del self.was_gpu_enabled
      return
    if not isinstance(was_gpu_enabled, bool):
      raise TypeError('was_gpu_enabled must be of type bool')
    self._was_gpu_enabled = was_gpu_enabled

  @property
  def was_internet_enabled(self) -> bool:
    return self._was_internet_enabled or False

  @was_internet_enabled.setter
  def was_internet_enabled(self, was_internet_enabled: Optional[bool]):
    if was_internet_enabled is None:
      del self.was_internet_enabled
      return
    if not isinstance(was_internet_enabled, bool):
      raise TypeError('was_internet_enabled must be of type bool')
    self._was_internet_enabled = was_internet_enabled

  @property
  def out_of_memory(self) -> bool:
    return self._out_of_memory

  @out_of_memory.setter
  def out_of_memory(self, out_of_memory: bool):
    if out_of_memory is None:
      del self.out_of_memory
      return
    if not isinstance(out_of_memory, bool):
      raise TypeError('out_of_memory must be of type bool')
    self._out_of_memory = out_of_memory

  @property
  def invalid_path_errors(self) -> bool:
    return self._invalid_path_errors

  @invalid_path_errors.setter
  def invalid_path_errors(self, invalid_path_errors: bool):
    if invalid_path_errors is None:
      del self.invalid_path_errors
      return
    if not isinstance(invalid_path_errors, bool):
      raise TypeError('invalid_path_errors must be of type bool')
    self._invalid_path_errors = invalid_path_errors

  @property
  def succeeded(self) -> bool:
    return self._succeeded

  @succeeded.setter
  def succeeded(self, succeeded: bool):
    if succeeded is None:
      del self.succeeded
      return
    if not isinstance(succeeded, bool):
      raise TypeError('succeeded must be of type bool')
    self._succeeded = succeeded

  @property
  def was_killed(self) -> bool:
    return self._was_killed

  @was_killed.setter
  def was_killed(self, was_killed: bool):
    if was_killed is None:
      del self.was_killed
      return
    if not isinstance(was_killed, bool):
      raise TypeError('was_killed must be of type bool')
    self._was_killed = was_killed


KernelSessionInfo._fields = [
  FieldMetadata("dockerfileUrl", "dockerfile_url", "_dockerfile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerHubUrl", "docker_hub_url", "_docker_hub_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImageDigest", "docker_image_digest", "_docker_image_digest", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImageId", "docker_image_id", "_docker_image_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImageName", "docker_image_name", "_docker_image_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("diskKbFree", "disk_kb_free", "_disk_kb_free", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("failureMessage", "failure_message", "_failure_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("exitCode", "exit_code", "_exit_code", int, 0, PredefinedSerializer()),
  FieldMetadata("queuedSeconds", "queued_seconds", "_queued_seconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outputSizeBytes", "output_size_bytes", "_output_size_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("runTimeSeconds", "run_time_seconds", "_run_time_seconds", float, 0.0, PredefinedSerializer()),
  FieldMetadata("usedAllSpace", "used_all_space", "_used_all_space", bool, False, PredefinedSerializer()),
  FieldMetadata("timeoutExceeded", "timeout_exceeded", "_timeout_exceeded", bool, False, PredefinedSerializer()),
  FieldMetadata("isValidStatus", "is_valid_status", "_is_valid_status", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("wasGpuEnabled", "was_gpu_enabled", "_was_gpu_enabled", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("wasInternetEnabled", "was_internet_enabled", "_was_internet_enabled", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outOfMemory", "out_of_memory", "_out_of_memory", bool, False, PredefinedSerializer()),
  FieldMetadata("invalidPathErrors", "invalid_path_errors", "_invalid_path_errors", bool, False, PredefinedSerializer()),
  FieldMetadata("succeeded", "succeeded", "_succeeded", bool, False, PredefinedSerializer()),
  FieldMetadata("wasKilled", "was_killed", "_was_killed", bool, False, PredefinedSerializer()),
]

