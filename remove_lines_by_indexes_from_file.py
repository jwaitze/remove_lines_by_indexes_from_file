# No imports necessary...

def remove_lines_by_indexes_from_file(filepath, indexes, buffer_size=10**6):
    indexes = set(indexes)
    with open(filepath, 'r+b') as f:
        position_last, position, position_next = 0, None, 0
        removals = []
        chunk, chunk_next = None, None
        line_last, line_index = b'', 0
        while position != position_next:
            if chunk is None:
                chunk = f.read(buffer_size)
                position = f.tell()
            else:
                chunk = chunk_next
                position_last = position
                position = position_next
            chunk_next = f.read(buffer_size)
            position_next = f.tell()
            lines = chunk.split(b'\n')
            if len(lines) > 0:
                lines[0] = line_last + lines[0]
            position_buffer = 0
            for line in lines[:-1 if position != position_next else None]:
                if line_index in indexes:
                    removals.append({
                        'position': position_last - len(line_last) + position_buffer,
                        'length': len(line) + 1
                        })
                line_index += 1
                position_buffer += len(line) + 1
            line_last = lines[-1]
        f.seek(0, 2)
        position_last = f.tell()
        length_removed, position_offset = 0, 0
        for i in range(len(removals) - 1, -1, -1):
            removal = removals[i]
            length_removed += removal['length']
            position_next_diff = position_offset + position_last - (removal['position'] + removal['length']) \
                                 if i + 1 == len(removals) else \
                                 position_offset + removals[i+1]['position'] - (removal['position'] + removal['length'])
            if position_next_diff < buffer_size:
                f.seek(removal['position'] + removal['length'])
                chunk = f.read(position_next_diff)
                f.seek(removal['position'])
                f.write(chunk)
            else:
                f.seek(0)
                chunks_amount = (position_next_diff // buffer_size) + 1
                for j in range(chunks_amount):
                    f.seek(removal['position'] + removal['length'] + j*buffer_size)
                    if j + 1 == chunks_amount:
                        chunk = f.read(position_next_diff % buffer_size)
                    else:
                        chunk = f.read(buffer_size)
                    f.seek(removal['position'] + j*buffer_size)
                    f.write(chunk)
            position_offset += position_next_diff
        if position_offset > 0:
            f.seek(position_last - length_removed)
            f.truncate()
