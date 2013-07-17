class RedisCommandsMixin(object):

    def append(self, key, value, callback=None):
        """
        Append a value to a key

            :param key:
            :param value:

        Complexity
        ----------
        O(1). The amortized time complexity is O(1) assuming the appended
        value is small and the already present value is of any size, since the
        dynamic string library used by Redis will double the free space
        available on every reallocation.
        """
        _args = ["APPEND"]
        _args.append(key)
        _args.append(value)
        self.send_message(_args, callback)

    def auth(self, password, callback=None):
        """
        Authenticate to the server

            :param password:
        """
        _args = ["AUTH"]
        _args.append(password)
        self.send_message(_args, callback)

    def bgrewriteaof(self, callback=None):
        """
        Asynchronously rewrite the append-only file
        """
        _args = ["BGREWRITEAOF"]
        self.send_message(_args, callback)

    def bgsave(self, callback=None):
        """
        Asynchronously save the dataset to disk
        """
        _args = ["BGSAVE"]
        self.send_message(_args, callback)

    def bitcount(self, key, start=None, end=None, callback=None):
        """
        Count set bits in a string

            :param key:
            :param start:
            :param end:

        Complexity
        ----------
        O(N)
        """
        _args = ["BITCOUNT"]
        _args.append(key)
        if start is not None:
            _args.append(start)
        if end is not None:
            _args.append(end)
        self.send_message(_args, callback)

    def bitop(self, operation, destkey, keys, callback=None):
        """
        Perform bitwise operations between strings

            :param operation:
            :param destkey:
            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N)
        """
        _args = ["BITOP"]
        _args.append(operation)
        _args.append(destkey)
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def blpop(self, keys, timeout, callback=None):
        """
        Remove and get the first element in a list, or block until one is
        available

            :param keys:
                string or list of strings
            :param timeout:

        Complexity
        ----------
        O(1)
        """
        _args = ["BLPOP"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        _args.append(timeout)
        self.send_message(_args, callback)

    def brpop(self, keys, timeout, callback=None):
        """
        Remove and get the last element in a list, or block until one is
        available

            :param keys:
                string or list of strings
            :param timeout:

        Complexity
        ----------
        O(1)
        """
        _args = ["BRPOP"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        _args.append(timeout)
        self.send_message(_args, callback)

    def brpoplpush(self, source, destination, timeout, callback=None):
        """
        Pop a value from a list, push it to another list and return it; or
        block until one is available

            :param source:
            :param destination:
            :param timeout:

        Complexity
        ----------
        O(1)
        """
        _args = ["BRPOPLPUSH"]
        _args.append(source)
        _args.append(destination)
        _args.append(timeout)
        self.send_message(_args, callback)

    def client_getname(self, callback=None):
        """
        Get the current connection name

        Complexity
        ----------
        O(1)
        """
        _args = ['CLIENT', 'GETNAME']
        self.send_message(_args, callback)

    def client_kill(self, ip_port, callback=None):
        """
        Kill the connection of a client

            :param ip_port:

        Complexity
        ----------
        O(N) where N is the number of client connections
        """
        _args = ['CLIENT', 'KILL']
        _args.append(ip_port)
        self.send_message(_args, callback)

    def client_list(self, callback=None):
        """
        Get the list of client connections

        Complexity
        ----------
        O(N) where N is the number of client connections
        """
        _args = ['CLIENT', 'LIST']
        self.send_message(_args, callback)

    def client_setname(self, connection_name, callback=None):
        """
        Set the current connection name

            :param connection_name:

        Complexity
        ----------
        O(1)
        """
        _args = ['CLIENT', 'SETNAME']
        _args.append(connection_name)
        self.send_message(_args, callback)

    def config_get(self, parameter, callback=None):
        """
        Get the value of a configuration parameter

            :param parameter:
        """
        _args = ['CONFIG', 'GET']
        _args.append(parameter)
        self.send_message(_args, callback)

    def config_resetstat(self, callback=None):
        """
        Reset the stats returned by INFO

        Complexity
        ----------
        O(1)
        """
        _args = ['CONFIG', 'RESETSTAT']
        self.send_message(_args, callback)

    def config_set(self, parameter, value, callback=None):
        """
        Set a configuration parameter to the given value

            :param parameter:
            :param value:
        """
        _args = ['CONFIG', 'SET']
        _args.append(parameter)
        _args.append(value)
        self.send_message(_args, callback)

    def dbsize(self, callback=None):
        """
        Return the number of keys in the selected database
        """
        _args = ["DBSIZE"]
        self.send_message(_args, callback)

    def debug_object(self, key, callback=None):
        """
        Get debugging information about a key

            :param key:
        """
        _args = ['DEBUG', 'OBJECT']
        _args.append(key)
        self.send_message(_args, callback)

    def debug_segfault(self, callback=None):
        """
        Make the server crash
        """
        _args = ['DEBUG', 'SEGFAULT']
        self.send_message(_args, callback)

    def decr(self, key, callback=None):
        """
        Decrement the integer value of a key by one

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["DECR"]
        _args.append(key)
        self.send_message(_args, callback)

    def decrby(self, key, decrement, callback=None):
        """
        Decrement the integer value of a key by the given number

            :param key:
            :param decrement:

        Complexity
        ----------
        O(1)
        """
        _args = ["DECRBY"]
        _args.append(key)
        _args.append(decrement)
        self.send_message(_args, callback)

    def delete(self, keys, callback=None):
        """
        Delete a key

            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of keys that will be removed. When a key to
        remove holds a value other than a string, the individual complexity
        for this key is O(M) where M is the number of elements in the list,
        set, sorted set or hash. Removing a single key that holds a string
        value is O(1).
        """
        _args = ["DEL"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def discard(self, callback=None):
        """
        Discard all commands issued after MULTI
        """
        _args = ["DISCARD"]
        self.send_message(_args, callback)

    def dump(self, key, callback=None):
        """
        Return a serialized version of the value stored at the specified key.

            :param key:

        Complexity
        ----------
        O(1) to access the key and additional O(N*M) to serialized it, where N
        is the number of Redis objects composing the value and M their average
        size. For small string values the time complexity is thus O(1)+O(1*M)
        where M is small, so simply O(1).
        """
        _args = ["DUMP"]
        _args.append(key)
        self.send_message(_args, callback)

    def echo(self, message, callback=None):
        """
        Echo the given string

            :param message:
        """
        _args = ["ECHO"]
        _args.append(message)
        self.send_message(_args, callback)

    def eval(self, script, keys, args, callback=None):
        """
        Execute a Lua script server side

            :param script:
            :param keys:
                string or list of strings
            :param args:
                string or list of strings

        Complexity
        ----------
        Depends on the script that is executed.
        """
        _args = ["EVAL"]
        _args.append(script)
        if not isinstance(keys, (list, tuple)):
            _args.append(1)
        else:
            _args.append(len(keys))
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        if not isinstance(args, (list, tuple)):
            _args.append(args)
        else:
            _args.extend(args)
        self.send_message(_args, callback)

    def evalsha(self, sha1, keys, args, callback=None):
        """
        Execute a Lua script server side

            :param sha1:
            :param keys:
                string or list of strings
            :param args:
                string or list of strings

        Complexity
        ----------
        Depends on the script that is executed.
        """
        _args = ["EVALSHA"]
        _args.append(sha1)
        if not isinstance(keys, (list, tuple)):
            _args.append(1)
        else:
            _args.append(len(keys))
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        if not isinstance(args, (list, tuple)):
            _args.append(args)
        else:
            _args.extend(args)
        self.send_message(_args, callback)

    def execute(self, callback=None):
        """
        Execute all commands issued after MULTI
        """
        _args = ["EXEC"]
        self.send_message(_args, callback)

    def exists(self, key, callback=None):
        """
        Determine if a key exists

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["EXISTS"]
        _args.append(key)
        self.send_message(_args, callback)

    def expire(self, key, seconds, callback=None):
        """
        Set a key's time to live in seconds

            :param key:
            :param seconds:

        Complexity
        ----------
        O(1)
        """
        _args = ["EXPIRE"]
        _args.append(key)
        _args.append(seconds)
        self.send_message(_args, callback)

    def expireat(self, key, timestamp, callback=None):
        """
        Set the expiration for a key as a UNIX timestamp

            :param key:
            :param timestamp:

        Complexity
        ----------
        O(1)
        """
        _args = ["EXPIREAT"]
        _args.append(key)
        _args.append(timestamp)
        self.send_message(_args, callback)

    def flushall(self, callback=None):
        """
        Remove all keys from all databases
        """
        _args = ["FLUSHALL"]
        self.send_message(_args, callback)

    def flushdb(self, callback=None):
        """
        Remove all keys from the current database
        """
        _args = ["FLUSHDB"]
        self.send_message(_args, callback)

    def get(self, key, callback=None):
        """
        Get the value of a key

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["GET"]
        _args.append(key)
        self.send_message(_args, callback)

    def getbit(self, key, offset, callback=None):
        """
        Returns the bit value at offset in the string value stored at key

            :param key:
            :param offset:

        Complexity
        ----------
        O(1)
        """
        _args = ["GETBIT"]
        _args.append(key)
        _args.append(offset)
        self.send_message(_args, callback)

    def getrange(self, key, start, end, callback=None):
        """
        Get a substring of the string stored at a key

            :param key:
            :param start:
            :param end:

        Complexity
        ----------
        O(N) where N is the length of the returned string. The complexity is
        ultimately determined by the returned length, but because creating a
        substring from an existing string is very cheap, it can be considered
        O(1) for small strings.
        """
        _args = ["GETRANGE"]
        _args.append(key)
        _args.append(start)
        _args.append(end)
        self.send_message(_args, callback)

    def getset(self, key, value, callback=None):
        """
        Set the string value of a key and return its old value

            :param key:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["GETSET"]
        _args.append(key)
        _args.append(value)
        self.send_message(_args, callback)

    def hdel(self, key, fields, callback=None):
        """
        Delete one or more hash fields

            :param key:
            :param fields:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of fields to be removed.
        """
        _args = ["HDEL"]
        _args.append(key)
        if not isinstance(fields, (list, tuple)):
            _args.append(fields)
        else:
            _args.extend(fields)
        self.send_message(_args, callback)

    def hexists(self, key, field, callback=None):
        """
        Determine if a hash field exists

            :param key:
            :param field:

        Complexity
        ----------
        O(1)
        """
        _args = ["HEXISTS"]
        _args.append(key)
        _args.append(field)
        self.send_message(_args, callback)

    def hget(self, key, field, callback=None):
        """
        Get the value of a hash field

            :param key:
            :param field:

        Complexity
        ----------
        O(1)
        """
        _args = ["HGET"]
        _args.append(key)
        _args.append(field)
        self.send_message(_args, callback)

    def hgetall(self, key, callback=None):
        """
        Get all the fields and values in a hash

            :param key:

        Complexity
        ----------
        O(N) where N is the size of the hash.
        """
        _args = ["HGETALL"]
        _args.append(key)
        self.send_message(_args, callback)

    def hincrby(self, key, field, increment, callback=None):
        """
        Increment the integer value of a hash field by the given number

            :param key:
            :param field:
            :param increment:

        Complexity
        ----------
        O(1)
        """
        _args = ["HINCRBY"]
        _args.append(key)
        _args.append(field)
        _args.append(increment)
        self.send_message(_args, callback)

    def hincrbyfloat(self, key, field, increment, callback=None):
        """
        Increment the float value of a hash field by the given amount

            :param key:
            :param field:
            :param increment:

        Complexity
        ----------
        O(1)
        """
        _args = ["HINCRBYFLOAT"]
        _args.append(key)
        _args.append(field)
        _args.append(increment)
        self.send_message(_args, callback)

    def hkeys(self, key, callback=None):
        """
        Get all the fields in a hash

            :param key:

        Complexity
        ----------
        O(N) where N is the size of the hash.
        """
        _args = ["HKEYS"]
        _args.append(key)
        self.send_message(_args, callback)

    def hlen(self, key, callback=None):
        """
        Get the number of fields in a hash

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["HLEN"]
        _args.append(key)
        self.send_message(_args, callback)

    def hmget(self, key, fields, callback=None):
        """
        Get the values of all the given hash fields

            :param key:
            :param fields:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of fields being requested.
        """
        _args = ["HMGET"]
        _args.append(key)
        if not isinstance(fields, (list, tuple)):
            _args.append(fields)
        else:
            _args.extend(fields)
        self.send_message(_args, callback)

    def hmset(self, key, field_dict, callback=None):
        """
        Set multiple hash fields to multiple values

            :param key:
            :param member_score_dict:
                key value dictionary

        Complexity
        ----------
        O(N) where N is the number of fields being set.
        """
        _args = ["HMSET"]
        _args.append(key)
        for field, value in field_dict.items():
            _args.append(field)
            _args.append(value)
        self.send_message(_args, callback)

    def hset(self, key, field, value, callback=None):
        """
        Set the string value of a hash field

            :param key:
            :param field:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["HSET"]
        _args.append(key)
        _args.append(field)
        _args.append(value)
        self.send_message(_args, callback)

    def hsetnx(self, key, field, value, callback=None):
        """
        Set the value of a hash field, only if the field does not exist

            :param key:
            :param field:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["HSETNX"]
        _args.append(key)
        _args.append(field)
        _args.append(value)
        self.send_message(_args, callback)

    def hvals(self, key, callback=None):
        """
        Get all the values in a hash

            :param key:

        Complexity
        ----------
        O(N) where N is the size of the hash.
        """
        _args = ["HVALS"]
        _args.append(key)
        self.send_message(_args, callback)

    def incr(self, key, callback=None):
        """
        Increment the integer value of a key by one

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["INCR"]
        _args.append(key)
        self.send_message(_args, callback)

    def incrby(self, key, increment, callback=None):
        """
        Increment the integer value of a key by the given amount

            :param key:
            :param increment:

        Complexity
        ----------
        O(1)
        """
        _args = ["INCRBY"]
        _args.append(key)
        _args.append(increment)
        self.send_message(_args, callback)

    def incrbyfloat(self, key, increment, callback=None):
        """
        Increment the float value of a key by the given amount

            :param key:
            :param increment:

        Complexity
        ----------
        O(1)
        """
        _args = ["INCRBYFLOAT"]
        _args.append(key)
        _args.append(increment)
        self.send_message(_args, callback)

    def info(self, section=None, callback=None):
        """
        Get information and statistics about the server

            :param section:
        """
        _args = ["INFO"]
        if section is not None:
            _args.append(section)
        self.send_message(_args, callback)

    def keys(self, pattern, callback=None):
        """
        Find all keys matching the given pattern

            :param pattern:

        Complexity
        ----------
        O(N) with N being the number of keys in the database, under the
        assumption that the key names in the database and the given pattern
        have limited length.
        """
        _args = ["KEYS"]
        _args.append(pattern)
        self.send_message(_args, callback)

    def lastsave(self, callback=None):
        """
        Get the UNIX time stamp of the last successful save to disk
        """
        _args = ["LASTSAVE"]
        self.send_message(_args, callback)

    def lindex(self, key, index, callback=None):
        """
        Get an element from a list by its index

            :param key:
            :param index:

        Complexity
        ----------
        O(N) where N is the number of elements to traverse to get to the
        element at index. This makes asking for the first or the last element
        of the list O(1).
        """
        _args = ["LINDEX"]
        _args.append(key)
        _args.append(index)
        self.send_message(_args, callback)

    def linsert(self, key, where, pivot, value, callback=None):
        """
        Insert an element before or after another element in a list

            :param key:
            :param where:
            :param pivot:
            :param value:

        Complexity
        ----------
        O(N) where N is the number of elements to traverse before seeing the
        value pivot. This means that inserting somewhere on the left end on
        the list (head) can be considered O(1) and inserting somewhere on the
        right end (tail) is O(N).
        """
        _args = ["LINSERT"]
        _args.append(key)
        _args.append(where)
        _args.append(pivot)
        _args.append(value)
        self.send_message(_args, callback)

    def llen(self, key, callback=None):
        """
        Get the length of a list

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["LLEN"]
        _args.append(key)
        self.send_message(_args, callback)

    def lpop(self, key, callback=None):
        """
        Remove and get the first element in a list

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["LPOP"]
        _args.append(key)
        self.send_message(_args, callback)

    def lpush(self, key, values, callback=None):
        """
        Prepend one or multiple values to a list

            :param key:
            :param values:
                string or list of strings

        Complexity
        ----------
        O(1)
        """
        _args = ["LPUSH"]
        _args.append(key)
        if not isinstance(values, (list, tuple)):
            _args.append(values)
        else:
            _args.extend(values)
        self.send_message(_args, callback)

    def lpushx(self, key, value, callback=None):
        """
        Prepend a value to a list, only if the list exists

            :param key:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["LPUSHX"]
        _args.append(key)
        _args.append(value)
        self.send_message(_args, callback)

    def lrange(self, key, start, stop, callback=None):
        """
        Get a range of elements from a list

            :param key:
            :param start:
            :param stop:

        Complexity
        ----------
        O(S+N) where S is the start offset and N is the number of elements in
        the specified range.
        """
        _args = ["LRANGE"]
        _args.append(key)
        _args.append(start)
        _args.append(stop)
        self.send_message(_args, callback)

    def lrem(self, key, count, value, callback=None):
        """
        Remove elements from a list

            :param key:
            :param count:
            :param value:

        Complexity
        ----------
        O(N) where N is the length of the list.
        """
        _args = ["LREM"]
        _args.append(key)
        _args.append(count)
        _args.append(value)
        self.send_message(_args, callback)

    def lset(self, key, index, value, callback=None):
        """
        Set the value of an element in a list by its index

            :param key:
            :param index:
            :param value:

        Complexity
        ----------
        O(N) where N is the length of the list. Setting either the first or
        the last element of the list is O(1).
        """
        _args = ["LSET"]
        _args.append(key)
        _args.append(index)
        _args.append(value)
        self.send_message(_args, callback)

    def ltrim(self, key, start, stop, callback=None):
        """
        Trim a list to the specified range

            :param key:
            :param start:
            :param stop:

        Complexity
        ----------
        O(N) where N is the number of elements to be removed by the operation.
        """
        _args = ["LTRIM"]
        _args.append(key)
        _args.append(start)
        _args.append(stop)
        self.send_message(_args, callback)

    def mget(self, keys, callback=None):
        """
        Get the values of all the given keys

            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of keys to retrieve.
        """
        _args = ["MGET"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def migrate(self, host, port, key, destination_db, timeout, callback=None):
        """
        Atomically transfer a key from a Redis instance to another one.

            :param host:
            :param port:
            :param key:
            :param destination_db:
            :param timeout:

        Complexity
        ----------
        This command actually executes a DUMP+DEL in the source instance, and
        a RESTORE in the target instance. See the pages of these commands for
        time complexity. Also an O(N) data transfer between the two instances
        is performed.
        """
        _args = ["MIGRATE"]
        _args.append(host)
        _args.append(port)
        _args.append(key)
        _args.append(destination_db)
        _args.append(timeout)
        self.send_message(_args, callback)

    def monitor(self, callback=None):
        """
        Listen for all requests received by the server in real time
        """
        _args = ["MONITOR"]
        self.send_message(_args, callback)

    def move(self, key, db, callback=None):
        """
        Move a key to another database

            :param key:
            :param db:

        Complexity
        ----------
        O(1)
        """
        _args = ["MOVE"]
        _args.append(key)
        _args.append(db)
        self.send_message(_args, callback)

    def mset(self, key_dict, callback=None):
        """
        Set multiple keys to multiple values

            :param member_score_dict:
                key value dictionary

        Complexity
        ----------
        O(N) where N is the number of keys to set.
        """
        _args = ["MSET"]
        for key, value in key_dict.items():
            _args.append(key)
            _args.append(value)
        self.send_message(_args, callback)

    def msetnx(self, key_dict, callback=None):
        """
        Set multiple keys to multiple values, only if none of the keys exist

            :param member_score_dict:
                key value dictionary

        Complexity
        ----------
        O(N) where N is the number of keys to set.
        """
        _args = ["MSETNX"]
        for key, value in key_dict.items():
            _args.append(key)
            _args.append(value)
        self.send_message(_args, callback)

    def multi(self, callback=None):
        """
        Mark the start of a transaction block
        """
        _args = ["MULTI"]
        self.send_message(_args, callback)

    def object(self, subcommand, argumentss=[], callback=None):
        """
        Inspect the internals of Redis objects

            :param subcommand:
            :param argumentss:
                string or list of strings

        Complexity
        ----------
        O(1) for all the currently implemented subcommands.
        """
        _args = ["OBJECT"]
        _args.append(subcommand)
        if not isinstance(argumentss, (list, tuple)):
            _args.append(argumentss)
        else:
            _args.extend(argumentss)
        self.send_message(_args, callback)

    def persist(self, key, callback=None):
        """
        Remove the expiration from a key

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["PERSIST"]
        _args.append(key)
        self.send_message(_args, callback)

    def pexpire(self, key, milliseconds, callback=None):
        """
        Set a key's time to live in milliseconds

            :param key:
            :param milliseconds:

        Complexity
        ----------
        O(1)
        """
        _args = ["PEXPIRE"]
        _args.append(key)
        _args.append(milliseconds)
        self.send_message(_args, callback)

    def pexpireat(self, key, milliseconds_timestamp, callback=None):
        """
        Set the expiration for a key as a UNIX timestamp specified in
        milliseconds

            :param key:
            :param milliseconds_timestamp:

        Complexity
        ----------
        O(1)
        """
        _args = ["PEXPIREAT"]
        _args.append(key)
        _args.append(milliseconds_timestamp)
        self.send_message(_args, callback)

    def ping(self, callback=None):
        """
        Ping the server
        """
        _args = ["PING"]
        self.send_message(_args, callback)

    def psetex(self, key, milliseconds, value, callback=None):
        """
        Set the value and expiration in milliseconds of a key

            :param key:
            :param milliseconds:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["PSETEX"]
        _args.append(key)
        _args.append(milliseconds)
        _args.append(value)
        self.send_message(_args, callback)

    def psubscribe(self, patterns, callback=None):
        """
        Listen for messages published to channels matching the given patterns

            :param member_score_dict:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of patterns the client is already
        subscribed to.
        """
        _args = ["PSUBSCRIBE"]
        if not isinstance(patterns, (list, tuple)):
            _args.append(patterns)
        else:
            _args.extend(patterns)
        self.send_message(_args, callback)

    def pttl(self, key, callback=None):
        """
        Get the time to live for a key in milliseconds

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["PTTL"]
        _args.append(key)
        self.send_message(_args, callback)

    def publish(self, channel, message, callback=None):
        """
        Post a message to a channel

            :param channel:
            :param message:

        Complexity
        ----------
        O(N+M) where N is the number of clients subscribed to the receiving
        channel and M is the total number of subscribed patterns (by any
        client).
        """
        _args = ["PUBLISH"]
        _args.append(channel)
        _args.append(message)
        self.send_message(_args, callback)

    def pubsub(self, subcommand, arguments=[], callback=None):
        """
        Inspect the state of the Pub/Sub subsystem

            :param subcommand:
            :param arguments:
                string or list of strings

        Complexity
        ----------
        O(N) for the CHANNELS subcommand, where N is the number of active
        channels, and assuming constant time pattern matching (relatively
        short channels and patterns). O(N) for the NUMSUB subcommand, where N
        is the number of requested channels. O(1) for the NUMPAT subcommand.
        """
        _args = ["PUBSUB"]
        _args.append(subcommand)
        if not isinstance(arguments, (list, tuple)):
            _args.append(arguments)
        else:
            _args.extend(arguments)
        self.send_message(_args, callback)

    def punsubscribe(self, patterns=[], callback=None):
        """
        Stop listening for messages posted to channels matching the given
        patterns

            :param patterns:
                string or list of strings

        Complexity
        ----------
        O(N+M) where N is the number of patterns the client is already
        subscribed and M is the number of total patterns subscribed in the
        system (by any client).
        """
        _args = ["PUNSUBSCRIBE"]
        if not isinstance(patterns, (list, tuple)):
            _args.append(patterns)
        else:
            _args.extend(patterns)
        self.send_message(_args, callback)

    def quit(self, callback=None):
        """
        Close the connection
        """
        _args = ["QUIT"]
        self.send_message(_args, callback)

    def randomkey(self, callback=None):
        """
        Return a random key from the keyspace

        Complexity
        ----------
        O(1)
        """
        _args = ["RANDOMKEY"]
        self.send_message(_args, callback)

    def rename(self, key, newkey, callback=None):
        """
        Rename a key

            :param key:
            :param newkey:

        Complexity
        ----------
        O(1)
        """
        _args = ["RENAME"]
        _args.append(key)
        _args.append(newkey)
        self.send_message(_args, callback)

    def renamenx(self, key, newkey, callback=None):
        """
        Rename a key, only if the new key does not exist

            :param key:
            :param newkey:

        Complexity
        ----------
        O(1)
        """
        _args = ["RENAMENX"]
        _args.append(key)
        _args.append(newkey)
        self.send_message(_args, callback)

    def restore(self, key, ttl, serialized_value, callback=None):
        """
        Create a key using the provided serialized value, previously obtained
        using DUMP.

            :param key:
            :param ttl:
            :param serialized_value:

        Complexity
        ----------
        O(1) to create the new key and additional O(N*M) to recostruct the
        serialized value, where N is the number of Redis objects composing the
        value and M their average size. For small string values the time
        complexity is thus O(1)+O(1*M) where M is small, so simply O(1).
        However for sorted set values the complexity is O(N*M*log(N)) because
        inserting values into sorted sets is O(log(N)).
        """
        _args = ["RESTORE"]
        _args.append(key)
        _args.append(ttl)
        _args.append(serialized_value)
        self.send_message(_args, callback)

    def rpop(self, key, callback=None):
        """
        Remove and get the last element in a list

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["RPOP"]
        _args.append(key)
        self.send_message(_args, callback)

    def rpoplpush(self, source, destination, callback=None):
        """
        Remove the last element in a list, append it to another list and
        return it

            :param source:
            :param destination:

        Complexity
        ----------
        O(1)
        """
        _args = ["RPOPLPUSH"]
        _args.append(source)
        _args.append(destination)
        self.send_message(_args, callback)

    def rpush(self, key, values, callback=None):
        """
        Append one or multiple values to a list

            :param key:
            :param values:
                string or list of strings

        Complexity
        ----------
        O(1)
        """
        _args = ["RPUSH"]
        _args.append(key)
        if not isinstance(values, (list, tuple)):
            _args.append(values)
        else:
            _args.extend(values)
        self.send_message(_args, callback)

    def rpushx(self, key, value, callback=None):
        """
        Append a value to a list, only if the list exists

            :param key:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["RPUSHX"]
        _args.append(key)
        _args.append(value)
        self.send_message(_args, callback)

    def sadd(self, key, members, callback=None):
        """
        Add one or more members to a set

            :param key:
            :param members:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of members to be added.
        """
        _args = ["SADD"]
        _args.append(key)
        if not isinstance(members, (list, tuple)):
            _args.append(members)
        else:
            _args.extend(members)
        self.send_message(_args, callback)

    def save(self, callback=None):
        """
        Synchronously save the dataset to disk
        """
        _args = ["SAVE"]
        self.send_message(_args, callback)

    def scard(self, key, callback=None):
        """
        Get the number of members in a set

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["SCARD"]
        _args.append(key)
        self.send_message(_args, callback)

    def script_exists(self, scripts, callback=None):
        """
        Check existence of scripts in the script cache.

            :param scripts:
                string or list of strings

        Complexity
        ----------
        O(N) with N being the number of scripts to check (so checking a single
        script is an O(1) operation).
        """
        _args = ['SCRIPT', 'EXISTS']
        if not isinstance(scripts, (list, tuple)):
            _args.append(scripts)
        else:
            _args.extend(scripts)
        self.send_message(_args, callback)

    def script_flush(self, callback=None):
        """
        Remove all the scripts from the script cache.

        Complexity
        ----------
        O(N) with N being the number of scripts in cache
        """
        _args = ['SCRIPT', 'FLUSH']
        self.send_message(_args, callback)

    def script_kill(self, callback=None):
        """
        Kill the script currently in execution.

        Complexity
        ----------
        O(1)
        """
        _args = ['SCRIPT', 'KILL']
        self.send_message(_args, callback)

    def script_load(self, script, callback=None):
        """
        Load the specified Lua script into the script cache.

            :param script:

        Complexity
        ----------
        O(N) with N being the length in bytes of the script body.
        """
        _args = ['SCRIPT', 'LOAD']
        _args.append(script)
        self.send_message(_args, callback)

    def sdiff(self, keys, callback=None):
        """
        Subtract multiple sets

            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the total number of elements in all given sets.
        """
        _args = ["SDIFF"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def sdiffstore(self, destination, keys, callback=None):
        """
        Subtract multiple sets and store the resulting set in a key

            :param destination:
            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the total number of elements in all given sets.
        """
        _args = ["SDIFFSTORE"]
        _args.append(destination)
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def select(self, index, callback=None):
        """
        Change the selected database for the current connection

            :param index:
        """
        _args = ["SELECT"]
        _args.append(index)
        self.send_message(_args, callback)

    def set(self, key, value, ex=None, px=None, condition=None, callback=None):
        """
        Set the string value of a key

            :param key:
            :param value:
            :param ex:
            :param px:
            :param condition:

        Complexity
        ----------
        O(1)
        """
        _args = ["SET"]
        _args.append(key)
        _args.append(value)
        if ex:
            _args.append("EX")
            _args.append(ex)
        if px:
            _args.append("PX")
            _args.append(px)
        if condition is not None:
            _args.append(condition)
        self.send_message(_args, callback)

    def setbit(self, key, offset, value, callback=None):
        """
        Sets or clears the bit at offset in the string value stored at key

            :param key:
            :param offset:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["SETBIT"]
        _args.append(key)
        _args.append(offset)
        _args.append(value)
        self.send_message(_args, callback)

    def setex(self, key, seconds, value, callback=None):
        """
        Set the value and expiration of a key

            :param key:
            :param seconds:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["SETEX"]
        _args.append(key)
        _args.append(seconds)
        _args.append(value)
        self.send_message(_args, callback)

    def setnx(self, key, value, callback=None):
        """
        Set the value of a key, only if the key does not exist

            :param key:
            :param value:

        Complexity
        ----------
        O(1)
        """
        _args = ["SETNX"]
        _args.append(key)
        _args.append(value)
        self.send_message(_args, callback)

    def setrange(self, key, offset, value, callback=None):
        """
        Overwrite part of a string at key starting at the specified offset

            :param key:
            :param offset:
            :param value:

        Complexity
        ----------
        O(1), not counting the time taken to copy the new string in place.
        Usually, this string is very small so the amortized complexity is
        O(1). Otherwise, complexity is O(M) with M being the length of the
        value argument.
        """
        _args = ["SETRANGE"]
        _args.append(key)
        _args.append(offset)
        _args.append(value)
        self.send_message(_args, callback)

    def shutdown(self, nosave=False, save=False, callback=None):
        """
        Synchronously save the dataset to disk and then shut down the server

            :param nosave:
            :param save:
        """
        _args = ["SHUTDOWN"]
        if nosave:
            _args.append("NOSAVE")
        if save:
            _args.append("SAVE")
        self.send_message(_args, callback)

    def sinter(self, keys, callback=None):
        """
        Intersect multiple sets

            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N*M) worst case where N is the cardinality of the smallest set and M
        is the number of sets.
        """
        _args = ["SINTER"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def sinterstore(self, destination, keys, callback=None):
        """
        Intersect multiple sets and store the resulting set in a key

            :param destination:
            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N*M) worst case where N is the cardinality of the smallest set and M
        is the number of sets.
        """
        _args = ["SINTERSTORE"]
        _args.append(destination)
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def sismember(self, key, member, callback=None):
        """
        Determine if a given value is a member of a set

            :param key:
            :param member:

        Complexity
        ----------
        O(1)
        """
        _args = ["SISMEMBER"]
        _args.append(key)
        _args.append(member)
        self.send_message(_args, callback)

    def slaveof(self, host, port, callback=None):
        """
        Make the server a slave of another instance, or promote it as master

            :param host:
            :param port:
        """
        _args = ["SLAVEOF"]
        _args.append(host)
        _args.append(port)
        self.send_message(_args, callback)

    def slowlog(self, subcommand, argument=None, callback=None):
        """
        Manages the Redis slow queries log

            :param subcommand:
            :param argument:
        """
        _args = ["SLOWLOG"]
        _args.append(subcommand)
        if argument is not None:
            _args.append(argument)
        self.send_message(_args, callback)

    def smembers(self, key, callback=None):
        """
        Get all the members in a set

            :param key:

        Complexity
        ----------
        O(N) where N is the set cardinality.
        """
        _args = ["SMEMBERS"]
        _args.append(key)
        self.send_message(_args, callback)

    def smove(self, source, destination, member, callback=None):
        """
        Move a member from one set to another

            :param source:
            :param destination:
            :param member:

        Complexity
        ----------
        O(1)
        """
        _args = ["SMOVE"]
        _args.append(source)
        _args.append(destination)
        _args.append(member)
        self.send_message(_args, callback)

    def sort(self, key, by=None, limit=None, get=tuple(), order=None, sorting=False, store=None, callback=None):
        """
        Sort the elements in a list, set or sorted set

            :param key:
            :param by:
            :param limit:
            :param get:
            :param order:
            :param sorting:
            :param store:

        Complexity
        ----------
        O(N+M*log(M)) where N is the number of elements in the list or set to
        sort, and M the number of returned elements. When the elements are not
        sorted, complexity is currently O(N) as there is a copy step that will
        be avoided in next releases.
        """
        _args = ["SORT"]
        _args.append(key)
        if by:
            _args.append("BY")
            _args.append(by)
        if limit:
            _args.append("LIMIT")
            offset, count = limit
            _args.append(offset)
            _args.append(count)
        for pattern in get:
            _args.append("GET")
            _args.append(pattern)
        if order is not None:
            _args.append(order)
        if sorting:
            _args.append("ALPHA")
        if store:
            _args.append("STORE")
            _args.append(store)
        self.send_message(_args, callback)

    def spop(self, key, callback=None):
        """
        Remove and return a random member from a set

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["SPOP"]
        _args.append(key)
        self.send_message(_args, callback)

    def srandmember(self, key, count=None, callback=None):
        """
        Get one or multiple random members from a set

            :param key:
            :param count:

        Complexity
        ----------
        Without the count argument O(1), otherwise O(N) where N is the
        absolute value of the passed count.
        """
        _args = ["SRANDMEMBER"]
        _args.append(key)
        if count is not None:
            _args.append(count)
        self.send_message(_args, callback)

    def srem(self, key, members, callback=None):
        """
        Remove one or more members from a set

            :param key:
            :param members:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of members to be removed.
        """
        _args = ["SREM"]
        _args.append(key)
        if not isinstance(members, (list, tuple)):
            _args.append(members)
        else:
            _args.extend(members)
        self.send_message(_args, callback)

    def strlen(self, key, callback=None):
        """
        Get the length of the value stored in a key

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["STRLEN"]
        _args.append(key)
        self.send_message(_args, callback)

    def subscribe(self, channels, callback=None):
        """
        Listen for messages published to the given channels

            :param member_score_dict:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of channels to subscribe to.
        """
        _args = ["SUBSCRIBE"]
        if not isinstance(channels, (list, tuple)):
            _args.append(channels)
        else:
            _args.extend(channels)
        self.send_message(_args, callback)

    def sunion(self, keys, callback=None):
        """
        Add multiple sets

            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the total number of elements in all given sets.
        """
        _args = ["SUNION"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def sunionstore(self, destination, keys, callback=None):
        """
        Add multiple sets and store the resulting set in a key

            :param destination:
            :param keys:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the total number of elements in all given sets.
        """
        _args = ["SUNIONSTORE"]
        _args.append(destination)
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def sync(self, callback=None):
        """
        Internal command used for replication
        """
        _args = ["SYNC"]
        self.send_message(_args, callback)

    def time(self, callback=None):
        """
        Return the current server time

        Complexity
        ----------
        O(1)
        """
        _args = ["TIME"]
        self.send_message(_args, callback)

    def ttl(self, key, callback=None):
        """
        Get the time to live for a key

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["TTL"]
        _args.append(key)
        self.send_message(_args, callback)

    def type(self, key, callback=None):
        """
        Determine the type stored at key

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["TYPE"]
        _args.append(key)
        self.send_message(_args, callback)

    def unsubscribe(self, channels=[], callback=None):
        """
        Stop listening for messages posted to the given channels

            :param channels:
                string or list of strings

        Complexity
        ----------
        O(N) where N is the number of clients already subscribed to a channel.
        """
        _args = ["UNSUBSCRIBE"]
        if not isinstance(channels, (list, tuple)):
            _args.append(channels)
        else:
            _args.extend(channels)
        self.send_message(_args, callback)

    def unwatch(self, callback=None):
        """
        Forget about all watched keys

        Complexity
        ----------
        O(1)
        """
        _args = ["UNWATCH"]
        self.send_message(_args, callback)

    def watch(self, keys, callback=None):
        """
        Watch the given keys to determine execution of the MULTI/EXEC block

            :param keys:
                string or list of strings

        Complexity
        ----------
        O(1) for every key.
        """
        _args = ["WATCH"]
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        self.send_message(_args, callback)

    def zadd(self, key, member_score_dict, callback=None):
        """
        Add one or more members to a sorted set, or update its score if it
        already exists

            :param key:
            :param member_score_dict:
                member score dictionary

        Complexity
        ----------
        O(log(N)) where N is the number of elements in the sorted set.
        """
        _args = ["ZADD"]
        _args.append(key)
        for member, score in member_score_dict.items():
            _args.append(score)
            _args.append(member)
        self.send_message(_args, callback)

    def zcard(self, key, callback=None):
        """
        Get the number of members in a sorted set

            :param key:

        Complexity
        ----------
        O(1)
        """
        _args = ["ZCARD"]
        _args.append(key)
        self.send_message(_args, callback)

    def zcount(self, key, min, max, callback=None):
        """
        Count the members in a sorted set with scores within the given values

            :param key:
            :param min:
            :param max:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M being the number of elements between min and max.
        """
        _args = ["ZCOUNT"]
        _args.append(key)
        _args.append(min)
        _args.append(max)
        self.send_message(_args, callback)

    def zincrby(self, key, increment, member, callback=None):
        """
        Increment the score of a member in a sorted set

            :param key:
            :param increment:
            :param member:

        Complexity
        ----------
        O(log(N)) where N is the number of elements in the sorted set.
        """
        _args = ["ZINCRBY"]
        _args.append(key)
        _args.append(increment)
        _args.append(member)
        self.send_message(_args, callback)

    def zinterstore(self, destination, keys, weights=tuple(), aggregate=None, callback=None):
        """
        Intersect multiple sorted sets and store the resulting sorted set in a
        new key

            :param destination:
            :param keys:
                string or list of strings
            :param weights:
            :param aggregate:

        Complexity
        ----------
        O(N*K)+O(M*log(M)) worst case with N being the smallest input sorted
        set, K being the number of input sorted sets and M being the number of
        elements in the resulting sorted set.
        """
        _args = ["ZINTERSTORE"]
        _args.append(destination)
        if not isinstance(keys, (list, tuple)):
            _args.append(1)
        else:
            _args.append(len(keys))
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        if len(weights):
            _args.append("WEIGHTS")
            _args.extend(weights)
        if aggregate:
            _args.append("AGGREGATE")
            _args.append(aggregate)
        self.send_message(_args, callback)

    def zrange(self, key, start, stop, withscores=False, callback=None):
        """
        Return a range of members in a sorted set, by index

            :param key:
            :param start:
            :param stop:
            :param withscores:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M the number of elements returned.
        """
        _args = ["ZRANGE"]
        _args.append(key)
        _args.append(start)
        _args.append(stop)
        if withscores:
            _args.append("WITHSCORES")
        self.send_message(_args, callback)

    def zrangebyscore(self, key, min, max, withscores=False, limit=None, callback=None):
        """
        Return a range of members in a sorted set, by score

            :param key:
            :param min:
            :param max:
            :param withscores:
            :param limit:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M the number of elements being returned. If M is constant (e.g. always
        asking for the first 10 elements with LIMIT), you can consider it
        O(log(N)).
        """
        _args = ["ZRANGEBYSCORE"]
        _args.append(key)
        _args.append(min)
        _args.append(max)
        if withscores:
            _args.append("WITHSCORES")
        if limit:
            _args.append("LIMIT")
            offset, count = limit
            _args.append(offset)
            _args.append(count)
        self.send_message(_args, callback)

    def zrank(self, key, member, callback=None):
        """
        Determine the index of a member in a sorted set

            :param key:
            :param member:

        Complexity
        ----------
        O(log(N))
        """
        _args = ["ZRANK"]
        _args.append(key)
        _args.append(member)
        self.send_message(_args, callback)

    def zrem(self, key, members, callback=None):
        """
        Remove one or more members from a sorted set

            :param key:
            :param members:
                string or list of strings

        Complexity
        ----------
        O(M*log(N)) with N being the number of elements in the sorted set and
        M the number of elements to be removed.
        """
        _args = ["ZREM"]
        _args.append(key)
        if not isinstance(members, (list, tuple)):
            _args.append(members)
        else:
            _args.extend(members)
        self.send_message(_args, callback)

    def zremrangebyrank(self, key, start, stop, callback=None):
        """
        Remove all members in a sorted set within the given indexes

            :param key:
            :param start:
            :param stop:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M the number of elements removed by the operation.
        """
        _args = ["ZREMRANGEBYRANK"]
        _args.append(key)
        _args.append(start)
        _args.append(stop)
        self.send_message(_args, callback)

    def zremrangebyscore(self, key, min, max, callback=None):
        """
        Remove all members in a sorted set within the given scores

            :param key:
            :param min:
            :param max:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M the number of elements removed by the operation.
        """
        _args = ["ZREMRANGEBYSCORE"]
        _args.append(key)
        _args.append(min)
        _args.append(max)
        self.send_message(_args, callback)

    def zrevrange(self, key, start, stop, withscores=False, callback=None):
        """
        Return a range of members in a sorted set, by index, with scores
        ordered from high to low

            :param key:
            :param start:
            :param stop:
            :param withscores:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M the number of elements returned.
        """
        _args = ["ZREVRANGE"]
        _args.append(key)
        _args.append(start)
        _args.append(stop)
        if withscores:
            _args.append("WITHSCORES")
        self.send_message(_args, callback)

    def zrevrangebyscore(self, key, max, min, withscores=False, limit=None, callback=None):
        """
        Return a range of members in a sorted set, by score, with scores
        ordered from high to low

            :param key:
            :param max:
            :param min:
            :param withscores:
            :param limit:

        Complexity
        ----------
        O(log(N)+M) with N being the number of elements in the sorted set and
        M the number of elements being returned. If M is constant (e.g. always
        asking for the first 10 elements with LIMIT), you can consider it
        O(log(N)).
        """
        _args = ["ZREVRANGEBYSCORE"]
        _args.append(key)
        _args.append(max)
        _args.append(min)
        if withscores:
            _args.append("WITHSCORES")
        if limit:
            _args.append("LIMIT")
            offset, count = limit
            _args.append(offset)
            _args.append(count)
        self.send_message(_args, callback)

    def zrevrank(self, key, member, callback=None):
        """
        Determine the index of a member in a sorted set, with scores ordered
        from high to low

            :param key:
            :param member:

        Complexity
        ----------
        O(log(N))
        """
        _args = ["ZREVRANK"]
        _args.append(key)
        _args.append(member)
        self.send_message(_args, callback)

    def zscore(self, key, member, callback=None):
        """
        Get the score associated with the given member in a sorted set

            :param key:
            :param member:

        Complexity
        ----------
        O(1)
        """
        _args = ["ZSCORE"]
        _args.append(key)
        _args.append(member)
        self.send_message(_args, callback)

    def zunionstore(self, destination, keys, weights=tuple(), aggregate=None, callback=None):
        """
        Add multiple sorted sets and store the resulting sorted set in a new
        key

            :param destination:
            :param keys:
                string or list of strings
            :param weights:
            :param aggregate:

        Complexity
        ----------
        O(N)+O(M log(M)) with N being the sum of the sizes of the input sorted
        sets, and M being the number of elements in the resulting sorted set.
        """
        _args = ["ZUNIONSTORE"]
        _args.append(destination)
        if not isinstance(keys, (list, tuple)):
            _args.append(1)
        else:
            _args.append(len(keys))
        if not isinstance(keys, (list, tuple)):
            _args.append(keys)
        else:
            _args.extend(keys)
        if len(weights):
            _args.append("WEIGHTS")
            _args.extend(weights)
        if aggregate:
            _args.append("AGGREGATE")
            _args.append(aggregate)
        self.send_message(_args, callback)
