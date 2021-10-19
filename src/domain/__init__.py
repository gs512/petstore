from dataclasses import dataclass, field
import uuid

@dataclass
class PetstoreEntity():
    id_: int = field(compare=True, init=False, default=None)

    def __post_init__(self):
        if self.id_ is None:
            self.id_ = uuid.uuid4()
