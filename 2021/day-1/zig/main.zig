const std = @import("std");
const fs = std.fs;
const io = std.io;
const fmt = std.fmt;
const debug = std.debug;

const expect = std.testing.expect;

var current: u16 = 0;
var previous: u16 = 0;
var total: u16 = 0;

pub fn main() anyerror!void {
    const file = try fs.cwd().openFile("../input", .{});
    defer file.close();

    var buf_reader = io.bufferedReader(file.reader());
    const in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        current = fmt.parseInt(u16, line, 10) catch |err| {
            debug.print("invalid number: {s}\n", .{err});
            continue;
        };

        if (previous == 0) {
            previous = current;
            continue;
        }

        if (current > previous) {
            total += 1;
        }

        // total += if (current > previous) 1;
        previous = current;
    }

    debug.print("total => {d}\n", .{total});
}
