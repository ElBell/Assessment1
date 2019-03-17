class Jumper:

    @staticmethod
    def jumps(height: int, jump_height: int) -> int:
        one_jumps = height % jump_height
        multiple_jumps = (height - one_jumps) / jump_height
        return int(one_jumps + multiple_jumps)
