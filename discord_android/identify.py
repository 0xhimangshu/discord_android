async def identify(self):
    payload = {
            'op': self.IDENTIFY,
            'd': {
                'token': self.token,
                'properties': {
                    'os': 'Discord Android',
                    'browser': 'Discord Android',
                    'device': 'Asus X515',
                },
                'compress': True,
                'large_threshold': 250,
            },
        }

    if self.shard_id is not None and self.shard_count is not None:
            payload['d']['shard'] = [self.shard_id, self.shard_count]

    state = self._connection

    if state._intents is not None:
        payload['d']['intents'] = state._intents.value

    await self.call_hooks("before_identify", self.shard_id, initial=self._initial_identify)
    await self.send_as_json(payload)
