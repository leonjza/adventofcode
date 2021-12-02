const std = @import("std");
const fs = std.fs;
const io = std.io;
const fmt = std.fmt;
const mem = std.mem;
const debug = std.debug;
const heap = std.heap;

// damn zig, y u no string helpers! : <
const String = @import("./zig-string.zig").String;

var horizontal: u16 = 0;
var depth: u16 = 0;

const Actions = enum { forward, down, up };

pub fn main() anyerror!void {
    const file = try fs.cwd().openFile("../input", .{});
    defer file.close();

    var buf_reader = io.bufferedReader(file.reader());
    const in_stream = buf_reader.reader();

    var buf: [10]u8 = undefined;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var s_buf: [20]u8 = undefined;
        var fba = heap.FixedBufferAllocator.init(&s_buf);
        var allocator = &fba.allocator;

        var string = String.init(allocator);
        defer string.deinit();

        try string.concat(line);
        const action_s = string.split(" ", 0).?;
        const amount_s = string.split(" ", 1).?;

        const amount = fmt.parseInt(u16, amount_s, 10) catch |err| {
            debug.print("invalid number: {s}\n", .{err});
            continue;
        };

        if (mem.eql(u8, action_s, "forward")) {
            horizontal += amount;
        }

        if (mem.eql(u8, action_s, "down")) {
            depth += amount;
        }

        if (mem.eql(u8, action_s, "up")) {
            depth -= amount;
        }
    }

    const total: u32 = @as(u32, horizontal) * depth;
    debug.print("total => {d}\n", .{total});
}
